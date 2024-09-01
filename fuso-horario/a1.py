def seconds_difference(time_1: float, time_2: float) -> float:
    """
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1

def hours_difference(time_1: float, time_2: float) -> float:
    """
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return (time_2 - time_1) / 3600.0

def to_float_hours(hours: int, minutes: int, seconds: int) -> float:
    """
    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return hours + minutes / 60.0 + seconds / 3600.0

def get_hours(seconds: int) -> int:
    """
    >>> get_hours(3800)
    1
    """
    return (seconds // 3600) % 24

def get_minutes(seconds: int) -> int:
    """
    >>> get_minutes(3800)
    3
    """
    return (seconds % 3600) // 60

def get_seconds(seconds: int) -> int:
    """
    >>> get_seconds(3800)
    20
    """
    return seconds % 60

def time_to_utc(utc_offset: float, time: float) -> float:
    """R
    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return (time - utc_offset) % 24

def time_from_utc(utc_offset: float, time: float) -> float:
    """
    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    """
    return (time + utc_offset) % 24