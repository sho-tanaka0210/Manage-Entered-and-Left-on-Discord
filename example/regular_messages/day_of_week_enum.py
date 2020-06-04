from enum import IntFlag, auto

class DayOfWeek(IntFlag):
    """
    Enum to set the day of the week.
    曜日を設定するためのEnum

    Parameters
    -----
    - Monday : int
        - value : 0
    - Tuesday : int
        - value : 1
    - Wednesday : int
        - value : 2
    - Thursday : int
        - value : 3
    - Friday : int
        - value : 4
    - Saturday : int
        - value : 5
    - Sunday : int
        - value: 6
    """
    Monday = 0
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()
