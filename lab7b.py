#!/usr/bin/env python3
# Student ID: swaghela

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum, normalized."""
    total_seconds = t1.hour * 3600 + t1.minute * 60 + t1.second
    total_seconds += t2.hour * 3600 + t2.minute * 60 + t2.second

    hour = (total_seconds // 3600) % 24
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60

    return Time(hour, minute, second)

def valid_time(t):
    """check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

def change_time(time, seconds):
    """Add or subtract seconds to/from a time object and normalize."""
    total = time.hour * 3600 + time.minute * 60 + time.second + seconds

    # Handle wrap-around and negative values by using modulo
    total = total % (24 * 3600)

    time.hour = (total // 3600) % 24
    time.minute = (total % 3600) // 60
    time.second = total % 60
    return None
