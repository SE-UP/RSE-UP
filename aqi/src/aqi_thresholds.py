"""
German Air Quality Index (AQI) Data Models

This module contains the data structures and threshold definitions for the
German AQI calculation.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Threshold:
    """
    Represents a single AQI threshold range for a pollutant.

    Attributes:
        label (str): The AQI category label (e.g., "good").
        low (float): The lower bound of the concentration range (inclusive).
        high (Optional[float]): The upper bound of the concentration range
            (inclusive). If None, the range extends to infinity.
    """

    label: str
    low: float
    high: Optional[float]


# Threshold definitions for each pollutant (hourly means in µg/m³)
PM10_THRESHOLDS: List[Threshold] = [
    Threshold("very good", 0, 9),
    Threshold("good", 10, 27),
    Threshold("moderate", 28, 54),
    Threshold("poor", 55, 90),
    Threshold("very poor", 91, None),
]

PM25_THRESHOLDS: List[Threshold] = [
    Threshold("very good", 0, 5),
    Threshold("good", 6, 15),
    Threshold("moderate", 16, 30),
    Threshold("poor", 31, 50),
    Threshold("very poor", 51, None),
]

O3_THRESHOLDS: List[Threshold] = [
    Threshold("very good", 0, 24),
    Threshold("good", 25, 72),
    Threshold("moderate", 73, 144),
    Threshold("poor", 145, 240),
    Threshold("very poor", 241, None),
]

NO2_THRESHOLDS: List[Threshold] = [
    Threshold("very good", 0, 10),
    Threshold("good", 11, 30),
    Threshold("moderate", 31, 60),
    Threshold("poor", 61, 100),
    Threshold("very poor", 101, None),
]

SO2_THRESHOLDS: List[Threshold] = [
    Threshold("very good", 0, 10),
    Threshold("good", 11, 30),
    Threshold("moderate", 31, 60),
    Threshold("poor", 61, 100),
    Threshold("very poor", 101, None),
]

THRESHOLDS_BY_POLLUTANT: Dict[str, List[Threshold]] = {
    "pm10": PM10_THRESHOLDS,
    "pm25": PM25_THRESHOLDS,
    "o3": O3_THRESHOLDS,
    "no2": NO2_THRESHOLDS,
    "so2": SO2_THRESHOLDS,
}
