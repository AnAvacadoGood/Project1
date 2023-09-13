#Programmed by Miko Tonthat
#Date: 07/23/19
#Description: This program returns the European and AM/PM time and adds/subtract them from each other.

#returns the European time you input
def from_european(s):
    """This function takes a string that has a European time in it
    as its argument and returns a new Clock object with the
    corresponding time.
    """
    hour = int(s[:2])
    if hour >= 24:
        hour = hour % 24
    minute = int(s[2:])
    return Clock(hour, minute)

#returns the AM/PM time you input into European time
def from_am_pm(s):
    """This function takes a string that has a time in
    AM/PM format it as its argument and returns a new Clock
    object with the corresponding time. 

    This function accepts the AM or PM in upper or lower case,
    with or without periods, presuming there will
    be at least one space after the digits.
    """
    s = s.split()
    if 'p' in s[1] or 'P' in s[1]:
        hr_and_min = s[0]
        hr_and_min = hr_and_min.split(":")
        hour = int(hr_and_min[0])
        hour = (hour % 12) + 12 # this makes 12 PM work perfectly!
        minute = int(hr_and_min[1])
        
    if 'a' in s[1] or 'A' in s[1]:
        hr_and_min = s[0]
        hr_and_min = hr_and_min.split(":")
        hour = int(hr_and_min[0]) % 12 # this makes 12 AM work perfectly
        minute = int(hr_and_min[1])
    return Clock(hour, minute)

class Clock:
    #initializer that forces the value into a certain range
    def __init__(self, hour, minute):
        """The constructor creates a new Clock with the given hour
        and minute. It ensures that, no matter what numbers are
        given, the hour is from 0 and 23 and the
        minute from 0 to 59.
        """
        self.hour = abs(hour)
        self.minute = minute
        if self.minute >= 59:
            self.hour = self.hour + self.minute // 60
            self.minute = self.minute % 60
    #outputs the time value into a string
    def __str__(self):
        """Return a string representing the time in 24-hour
        European notation
        """
        return format(self.hour, '02d') + format(self.minute, '02d') 
    #converts the hours into minutes and adds it into the minutes
    def total_minutes(self):
        """ This is a utility function that takes a Clock
        object and returns the number of minutes past
        midnight that it represents. (I am providing this
        code for you.)
        """
        return self.hour * 60 + self.minute
    #adds both times
    def add(self, other):
        """Return a new Clock object that is the result
        of adding self to other.
        """
        sum_hour = self.hour + other.hour
        if sum_hour >= 24:
            sum_hour = sum_hour % 24
        sum_minutes = self.minute + other.minute
        result = Clock(sum_hour, sum_minutes)
        return result
    #subtracts both times from each other
    def subtract(self, other):
        """Return a new Clock object that is the result
        of subtracting the smaller time from the larger time.
        """
        #grabs the smaller value and subtracts from the larger value
        if self.hour > other.hour:
            difference_hour = self.hour - other.hour
            difference_minutes = self.minute - other.minute
        else:
            difference_hour = other.hour - self.hour
            difference_minutes = other.minute - self.minute
        if difference_minutes // 60 < 0:
            difference_hour += difference_minutes // 60
            difference_minutes += 60
        result = Clock(difference_hour, difference_minutes)
        return result

