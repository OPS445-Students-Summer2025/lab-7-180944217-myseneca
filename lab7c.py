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

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from midnight'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    seconds %= 86400  # Ensure it's within a single day
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects using seconds conversion"""
    sec1 = time_to_sec(t1)
    sec2 = time_to_sec(t2)
    total = sec1 + sec2
    return sec_to_time(total)

def change_time(time, seconds):
    """Change time object by seconds using conversion functions"""
    total = time_to_sec(time) + seconds
    new_time = sec_to_time(total)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True


