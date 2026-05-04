"""
German Air Quality Index (AQI) Calculator

This module implements the official methodology for calculating the German
Air Quality Index (AQI) as defined by the German Environment Agency (UBA
Umweltbundesamt).

The AQI classifies air quality into five categories based on concentrations
of five pollutants:
- PM₁₀: Particulate matter ≤ 10 µm
- PM₂.₅: Particulate matter ≤ 2.5 µm
- O₃: Ozone
- NO₂: Nitrogen dioxide
- SO₂: Sulfur dioxide

Each pollutant concentration is mapped to one of five categories: "very good",
"good", "moderate", "poor", "very poor". The overall AQI for a given time
point is calculated by the "maximum operator rule", taking the worst (highest)
category among all pollutants.

Thresholds are based on hourly mean values in µg/m³, sourced from:
https://www.umweltbundesamt.de/en/calculation-base-air-quality-index

Note: For O₃, we adjust the boundary at 24 µg/m³ to avoid overlap between
"very good" (0–24) and "good" (25–72).
"""

import logging
from typing import Any, Mapping, Optional

import pandas as pd

from aqi_thresholds import THRESHOLDS_BY_POLLUTANT

logger = logging.getLogger(__name__)

# AQI category definitions
AQI_LEVELS = ["very good", "good", "moderate", "poor", "very poor"]
AQI_SCORE = {label: i for i, label in enumerate(AQI_LEVELS, start=1)}


def classify_pollutant(
    value: Optional[float], pollutant: str
) -> Optional[str]:
    """
    Classify a single pollutant concentration value into an AQI category.

    Args:
        value (Optional[float]): The pollutant concentration in µg/m³. If None
            or NaN, returns None.
        pollutant (str): The pollutant key (e.g., "pm10", "o3"). Must be a key
            in THRESHOLDS_BY_POLLUTANT. Maps to: "pm10" (PM₁₀: coarse
            particulate matter ≤ 10 µm), "pm25" (PM₂.₅: fine particulate
            matter ≤ 2.5 µm), "o3" (O₃: ozone), "no2" (NO₂: nitrogen dioxide),
            "so2" (SO₂: sulfur dioxide).

    Returns:
        Optional[str]: The AQI category label (e.g., "good"), or None if value
            is missing or invalid.

    Raises:
        ValueError: If pollutant is not recognized.
    """

    if value is None or pd.isna(value):
        logger.debug(
            "Skipping classification for %s: value is NaN/None", pollutant
        )
        return None

    if pollutant not in THRESHOLDS_BY_POLLUTANT:
        logger.error("Unknown pollutant: %s", pollutant)
        raise ValueError(f"Unknown pollutant: {pollutant}")

    thresholds = THRESHOLDS_BY_POLLUTANT[pollutant]

    for t in thresholds:
        if t.high is None:
            if value >= t.low:
                logger.debug(
                    "Classified %s=%.2f as '%s'", pollutant, value, t.label
                )
                return t.label
        else:
            if t.low <= value <= t.high:
                logger.debug(
                    "Classified %s=%.2f as '%s'", pollutant, value, t.label
                )
                return t.label

    # Should not reach here if thresholds are defined correctly
    logger.error(
        "No threshold matched for pollutant '%s' with value %.2f",
        pollutant,
        value,
    )
    raise ValueError(
        f"No threshold found for pollutant '{pollutant}' with value {value}"
    )


def compute_row_aqi(row: Mapping[str, Any]) -> Optional[str]:
    """
    Compute the overall AQI category for a single data row (e.g., one hour at
    one station).

    Applies the maximum operator rule: the overall AQI is the worst (highest
    score) category among all measured pollutants in the row. Pollutant columns
    are expected to be named "pm10", "pm25", "o3", "no2", "so2" (lowercase,
    matching the keys in THRESHOLDS_BY_POLLUTANT). Missing or NaN values for
    pollutants are ignored.

    Args:
        row: A pandas series like object with pollutant columns (e.g., "pm10",
            "o3", etc.). Columns should be named "pm10", "pm25", "o3", "no2",
            "so2".

    Returns:
        Optional[str]: The overall AQI category label ("very good", "good",
            etc.), or None if no pollutants are measured.
    """

    labels = []

    for col in THRESHOLDS_BY_POLLUTANT:
        if col in row and not pd.isna(row[col]):
            label = classify_pollutant(row[col], col)
            if label is not None:
                labels.append(label)

    if not labels:
        logger.warning(
            "No valid pollutant readings found in row; returning None"
        )
        return None

    # Select the worst (highest score) category
    worst_label = max(labels, key=lambda lbl: AQI_SCORE[lbl])
    logger.debug("Row AQI: %s (from %s)", worst_label, labels)
    return worst_label


def compute_aqi_for_dataframe(df: pd.DataFrame) -> "pd.Series[Any]":
    """
    Compute AQI categories for all rows in a DataFrame.

    Args:
        df: A pandas DataFrame with pollutant columns named "pm10", "pm25",
            "o3", "no2", "so2".

    Returns:
        A pandas series of AQI category labels, one per row ("very good",
        "good", etc., or None).
    """
    logger.info("Computing AQI for %d rows", len(df))
    result: "pd.Series[Any]" = df.apply(compute_row_aqi, axis=1)
    logger.info("AQI computation complete")
    return result


def main() -> None:  # pragma no cover
    """
    Demonstration of the German AQI calculator with example data.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s %(name)s: %(message)s",
    )
    print("German Air Quality Index (AQI) Calculator Demonstration")
    print("=" * 55)

    # Example pollutant concentrations (µg/m³)
    example_data = {
        "pm10": 25.0,  # Particulate matter ≤ 10 µm
        "pm25": 12.0,  # Particulate matter ≤ 2.5 µm
        "o3": 45.0,  # Ozone
        "no2": 20.0,  # Nitrogen dioxide
        "so2": 8.0,  # Sulfur dioxide
    }

    print("AQI Analyzer: Single Row Demonstration")
    for pollutant, value in example_data.items():
        print(f"  {pollutant.upper()}: {value} µg/m³")

    print("\nIndividual pollutant classifications:")
    classifications = {}
    for pollutant, value in example_data.items():
        category = classify_pollutant(value, pollutant)
        classifications[pollutant] = category
        print(f"  {pollutant.upper()}: {category}")

    print("\nOverall AQI calculation (maximum operator rule):")
    overall_aqi = compute_row_aqi(example_data)
    print(f"  Overall AQI: {overall_aqi}")

    print("\nAQI Categories (worst to best):")
    for level in reversed(AQI_LEVELS):
        marker = " ←" if level == overall_aqi else ""
        print(f"  {level}{marker}")


if __name__ == "__main__":  # pragma no cover
    main()
