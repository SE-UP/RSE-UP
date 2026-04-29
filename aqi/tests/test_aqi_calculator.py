import pandas as pd
import pytest

from aqi_calculator import (
    AQI_LEVELS,
    AQI_SCORE,
    classify_pollutant,
    compute_aqi_for_dataframe,
    compute_row_aqi,
)
from aqi_thresholds import THRESHOLDS_BY_POLLUTANT

# Each tuple: (pollutant, value, expected_category).
# Values are mid-class representatives, not boundary values, those are
# covered in TestBoundaryValues.
CLASSIFY_EQUIVALENCE_CLASSES = [
    # PM10 equivalence classes
    ("pm10", 5, "very good"),
    ("pm10", 18, "good"),
    ("pm10", 40, "moderate"),
    ("pm10", 70, "poor"),
    ("pm10", 120, "very poor"),
    # PM25 equivalence classes
    ("pm25", 3, "very good"),
    ("pm25", 10, "good"),
    ("pm25", 22, "moderate"),
    ("pm25", 40, "poor"),
    ("pm25", 60, "very poor"),
    # O3 equivalence classes
    ("o3", 12, "very good"),
    ("o3", 45, "good"),
    ("o3", 100, "moderate"),
    ("o3", 180, "poor"),
    ("o3", 250, "very poor"),
    # NO2 equivalence classes
    ("no2", 5, "very good"),
    ("no2", 20, "good"),
    ("no2", 45, "moderate"),
    ("no2", 80, "poor"),
    ("no2", 120, "very poor"),
    # SO2 equivalence classes
    ("so2", 5, "very good"),
    ("so2", 20, "good"),
    ("so2", 45, "moderate"),
    ("so2", 80, "poor"),
    ("so2", 120, "very poor"),
]

# Kept separate because the third tuple element is an exception type,
# not a return value.
INVALID_POLLUTANT_CLASS = [
    ("invalid_pollutant", 10, ValueError),
]


# Each tuple: (row_data_dict, expected_aqi).
# Omitted: false/invalid-key class (e.g. {"unknown": 10}).
# compute_row_aqi only iterates over known pollutant keys, so unknown keys are
# silently ignored, same result as an empty row, already covered by ({}, None).
ROW_AQI_EQUIVALENCE_CLASSES = [
    # Single pollutant classes
    ({"pm10": 5}, "very good"),
    ({"pm10": 18}, "good"),
    ({"pm10": 40}, "moderate"),
    ({"pm10": 70}, "poor"),
    ({"pm10": 120}, "very poor"),
    # Multiple pollutants same category
    ({"pm10": 5, "pm25": 3, "o3": 12}, "very good"),
    ({"pm10": 18, "pm25": 10, "o3": 45}, "good"),
    # Multiple pollutants different categories (test max rule)
    ({"pm10": 5, "pm25": 60}, "very poor"),
    ({"pm10": 18, "o3": 100}, "moderate"),
    ({"pm10": 40, "pm25": 22, "no2": 80}, "poor"),
    # Missing pollutant classes
    ({"pm10": 5, "pm25": None}, "very good"),
    ({"pm10": None, "pm25": 3}, "very good"),
    ({"pm10": float("nan"), "pm25": 3}, "very good"),
    ({}, None),
    ({"pm10": None, "pm25": None}, None),
]


# Tests for classify_pollutant: maps a single concentration value to an
# AQI category.
class TestClassifyPollutant:
    @pytest.mark.parametrize(
        "pollutant,value,expected", CLASSIFY_EQUIVALENCE_CLASSES
    )
    def test_equivalence_classes(self, pollutant, value, expected):
        """Test equivalence classes for classify_pollutant function."""
        assert classify_pollutant(value, pollutant) == expected

    @pytest.mark.parametrize(
        "pollutant,value,expected_exception", INVALID_POLLUTANT_CLASS
    )
    def test_invalid_pollutant_equivalence_class(
        self, pollutant, value, expected_exception
    ):
        """Test invalid pollutant equivalence class."""
        with pytest.raises(expected_exception, match="Unknown pollutant"):
            classify_pollutant(value, pollutant)

    def test_none_value_equivalence_class(self):
        """Test None value equivalence class."""
        assert classify_pollutant(None, "pm10") is None

    def test_nan_value_equivalence_class(self):
        """Test NaN value equivalence class."""
        assert classify_pollutant(float("nan"), "pm10") is None

    def test_invalid_values_raise_exception(self):
        # Test invalid values (negatives) raise ValueError when no
        # threshold matches
        with pytest.raises(ValueError, match="No threshold found"):
            classify_pollutant(-1, "pm10")
        with pytest.raises(ValueError, match="No threshold found"):
            classify_pollutant(-5, "o3")


# Tests for compute_row_aqi: applies the max rule across all pollutants
# in one row.
class TestComputeRowAqi:
    @pytest.mark.parametrize(
        "row_data,expected_aqi", ROW_AQI_EQUIVALENCE_CLASSES
    )
    def test_equivalence_classes(self, row_data, expected_aqi):
        """Test equivalence classes for compute_row_aqi function."""
        row = pd.Series(row_data)
        assert compute_row_aqi(row) == expected_aqi

    # Named tests below overlap with the parametrized cases but give
    # clearer failure messages.
    def test_single_pollutant(self):
        row = pd.Series({"pm10": 20})  # Good
        assert compute_row_aqi(row) == "good"

        row = pd.Series({"o3": 150})  # Poor
        assert compute_row_aqi(row) == "poor"

    def test_multiple_pollutants_same_category(self):
        row = pd.Series({"pm10": 20, "pm25": 10})  # Both good
        assert compute_row_aqi(row) == "good"

    def test_multiple_pollutants_different_categories(self):
        row = pd.Series({"pm10": 20, "o3": 150})  # Good and poor gives poor
        assert compute_row_aqi(row) == "poor"

        row = pd.Series({"pm10": 100, "pm25": 60, "o3": 50})
        # Very poor + very poor + good -> very poor
        assert compute_row_aqi(row) == "very poor"

    def test_missing_pollutants(self):
        # Both None and NaN count as missing and are skipped.
        row = pd.Series({"pm10": None, "pm25": 10})
        assert compute_row_aqi(row) == "good"

        row = pd.Series({"pm10": float("nan"), "pm25": 10})
        assert compute_row_aqi(row) == "good"

    def test_no_valid_pollutants(self):
        row = pd.Series({"pm10": None, "pm25": None})
        assert compute_row_aqi(row) is None

        row = pd.Series({})
        assert compute_row_aqi(row) is None


# Tests for compute_aqi_for_dataframe: applies compute_row_aqi to every
# row in a DataFrame.
class TestComputeAqiForDataframe:
    def test_dataframe_computation(self):
        # row 0: good / very good / very good  -> good
        # row 1: moderate / moderate / moderate -> moderate
        # row 2: very poor / very poor / poor   -> very poor
        df = pd.DataFrame(
            {
                "pm10": [10, 50, 100],
                "pm25": [5, 20, 60],
                "o3": [20, 80, 150],
            }
        )
        result = compute_aqi_for_dataframe(df)
        expected = pd.Series(["good", "moderate", "very poor"])
        pd.testing.assert_series_equal(result, expected)

    def test_empty_dataframe(self):
        # An empty DataFrame should return an empty Series without errors.
        df = pd.DataFrame()
        result = compute_aqi_for_dataframe(df)
        assert len(result) == 0


class TestBoundaryValues:
    """Test boundary values at category thresholds."""

    def test_pm10_boundary_values(self):
        """
        Test PM10 boundary values: very good (0-9), good (10-27),
        moderate (28-54), poor (55-90), very poor (91+).
        """
        # Very good boundaries
        assert classify_pollutant(0, "pm10") == "very good"  # Lower boundary
        assert classify_pollutant(9, "pm10") == "very good"  # Upper boundary
        assert (
            classify_pollutant(10, "pm10") == "good"
        )  # Next category lower boundary

        # Good boundaries
        assert classify_pollutant(10, "pm10") == "good"  # Lower boundary
        assert classify_pollutant(27, "pm10") == "good"  # Upper boundary
        assert (
            classify_pollutant(28, "pm10") == "moderate"
        )  # Next category lower boundary

        # Moderate boundaries
        assert classify_pollutant(28, "pm10") == "moderate"  # Lower boundary
        assert classify_pollutant(54, "pm10") == "moderate"  # Upper boundary
        assert (
            classify_pollutant(55, "pm10") == "poor"
        )  # Next category lower boundary

        # Poor boundaries
        assert classify_pollutant(55, "pm10") == "poor"  # Lower boundary
        assert classify_pollutant(90, "pm10") == "poor"  # Upper boundary
        assert (
            classify_pollutant(91, "pm10") == "very poor"
        )  # Next category lower boundary

        # Very poor boundaries (no upper bound)
        assert classify_pollutant(91, "pm10") == "very poor"  # Lower boundary
        assert classify_pollutant(1000, "pm10") == "very poor"  # Far above

    def test_pm25_boundary_values(self):
        """
        Test PM2.5 boundary values: very good (0-5), good (6-15),
        moderate (16-30), poor (31-50), very poor (51+).
        """
        # Very good boundaries
        assert classify_pollutant(0, "pm25") == "very good"  # Lower boundary
        assert classify_pollutant(5, "pm25") == "very good"  # Upper boundary
        assert (
            classify_pollutant(6, "pm25") == "good"
        )  # Next category lower boundary

        # Good boundaries
        assert classify_pollutant(6, "pm25") == "good"  # Lower boundary
        assert classify_pollutant(15, "pm25") == "good"  # Upper boundary
        assert (
            classify_pollutant(16, "pm25") == "moderate"
        )  # Next category lower boundary

        # Moderate boundaries
        assert classify_pollutant(16, "pm25") == "moderate"  # Lower boundary
        assert classify_pollutant(30, "pm25") == "moderate"  # Upper boundary
        assert (
            classify_pollutant(31, "pm25") == "poor"
        )  # Next category lower boundary

        # Poor boundaries
        assert classify_pollutant(31, "pm25") == "poor"  # Lower boundary
        assert classify_pollutant(50, "pm25") == "poor"  # Upper boundary
        assert (
            classify_pollutant(51, "pm25") == "very poor"
        )  # Next category lower boundary

        # Very poor boundaries
        assert classify_pollutant(51, "pm25") == "very poor"  # Lower boundary

    def test_o3_boundary_values(self):
        """
        Test O3 boundary values: very good (0-24), good (25-72),
        moderate (73-144), poor (145-240), very poor (241+).
        """
        # Very good boundaries
        assert classify_pollutant(0, "o3") == "very good"  # Lower boundary
        assert classify_pollutant(24, "o3") == "very good"  # Upper boundary
        assert (
            classify_pollutant(25, "o3") == "good"
        )  # Next category lower boundary

        # Good boundaries
        assert classify_pollutant(25, "o3") == "good"  # Lower boundary
        assert classify_pollutant(72, "o3") == "good"  # Upper boundary
        assert (
            classify_pollutant(73, "o3") == "moderate"
        )  # Next category lower boundary

        # Moderate boundaries
        assert classify_pollutant(73, "o3") == "moderate"  # Lower boundary
        assert classify_pollutant(144, "o3") == "moderate"  # Upper boundary
        assert (
            classify_pollutant(145, "o3") == "poor"
        )  # Next category lower boundary

        # Poor boundaries
        assert classify_pollutant(145, "o3") == "poor"  # Lower boundary
        assert classify_pollutant(240, "o3") == "poor"  # Upper boundary
        assert (
            classify_pollutant(241, "o3") == "very poor"
        )  # Next category lower boundary

        # Very poor boundaries
        assert classify_pollutant(241, "o3") == "very poor"  # Lower boundary

    def test_no2_boundary_values(self):
        """
        Test NO2 boundary values: very good (0-10), good (11-30),
        moderate (31-60), poor (61-100), very poor (101+).
        """
        # Very good boundaries
        assert classify_pollutant(0, "no2") == "very good"  # Lower boundary
        assert classify_pollutant(10, "no2") == "very good"  # Upper boundary
        assert (
            classify_pollutant(11, "no2") == "good"
        )  # Next category lower boundary

        # Good boundaries
        assert classify_pollutant(11, "no2") == "good"  # Lower boundary
        assert classify_pollutant(30, "no2") == "good"  # Upper boundary
        assert (
            classify_pollutant(31, "no2") == "moderate"
        )  # Next category lower boundary

        # Moderate boundaries
        assert classify_pollutant(31, "no2") == "moderate"  # Lower boundary
        assert classify_pollutant(60, "no2") == "moderate"  # Upper boundary
        assert (
            classify_pollutant(61, "no2") == "poor"
        )  # Next category lower boundary

        # Poor boundaries
        assert classify_pollutant(61, "no2") == "poor"  # Lower boundary
        assert classify_pollutant(100, "no2") == "poor"  # Upper boundary
        assert (
            classify_pollutant(101, "no2") == "very poor"
        )  # Next category lower boundary

        # Very poor boundaries
        assert classify_pollutant(101, "no2") == "very poor"  # Lower boundary

    def test_so2_boundary_values(self):
        """
        Test SO2 boundary values: very good (0-10), good (11-30),
        moderate (31-60), poor (61-100), very poor (101+).
        """
        # Very good boundaries
        assert classify_pollutant(0, "so2") == "very good"  # Lower boundary
        assert classify_pollutant(10, "so2") == "very good"  # Upper boundary
        assert (
            classify_pollutant(11, "so2") == "good"
        )  # Next category lower boundary

        # Good boundaries
        assert classify_pollutant(11, "so2") == "good"  # Lower boundary
        assert classify_pollutant(30, "so2") == "good"  # Upper boundary
        assert (
            classify_pollutant(31, "so2") == "moderate"
        )  # Next category lower boundary

        # Moderate boundaries
        assert classify_pollutant(31, "so2") == "moderate"  # Lower boundary
        assert classify_pollutant(60, "so2") == "moderate"  # Upper boundary
        assert (
            classify_pollutant(61, "so2") == "poor"
        )  # Next category lower boundary

        # Poor boundaries
        assert classify_pollutant(61, "so2") == "poor"  # Lower boundary
        assert classify_pollutant(100, "so2") == "poor"  # Upper boundary
        assert (
            classify_pollutant(101, "so2") == "very poor"
        )  # Next category lower boundary

        # Very poor boundaries
        assert classify_pollutant(101, "so2") == "very poor"  # Lower boundary


class TestThresholds:
    def test_thresholds_coverage(self):
        # Ensure all pollutants have thresholds
        expected_pollutants = {"pm10", "pm25", "o3", "no2", "so2"}
        assert set(THRESHOLDS_BY_POLLUTANT.keys()) == expected_pollutants

    def test_aqi_levels(self):
        # AQI_SCORE maps each category to a number so the max rule can
        # compare them.
        assert AQI_LEVELS == [
            "very good",
            "good",
            "moderate",
            "poor",
            "very poor",
        ]
        assert AQI_SCORE == {
            "very good": 1,
            "good": 2,
            "moderate": 3,
            "poor": 4,
            "very poor": 5,
        }
