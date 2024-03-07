#! /usr/bin/env python3

import sys
from parse_temps import parse_raw_temps



def linear_interpolation(times, core_temps):
    """
    Perform linear piecewise interpolation on temperature data.

    :param times: represents the x-coordinates of data points.
    :param core_temps: A list of temperature values corresponding to the timestamps.
    :return: A list of interpolated temperature data as (x_min, x_max, a, b) tuples.
    """
    interpolated_data = []
    for i in range(len(times) - 1):
        x1, y1 = times[i], core_temps[i]
        x2, y2 = times[i + 1], core_temps[i + 1]
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        interpolated_data.append((x1, x2, m, b))
    
    return interpolated_data
