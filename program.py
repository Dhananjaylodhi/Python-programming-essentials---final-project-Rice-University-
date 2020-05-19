import datetime


def days_in_month(year, month):
    """
    Inputs:
    year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
                  representing the year
    month - an integer between 1 and 12 representing the month

    Returns:
    The number of days in the input month.
    """
    thirty_days_months = [4, 6, 9, 11]  # months having 30 days
    thirty_one_days_months = [1, 3, 5, 7, 8, 10, 12]  # months having 31 days

    leap_counter = 0  # increases if the year is leap year
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap_counter += 1
            else:
                leap_counter += 0
        else:
            leap_counter += 1
    else:
        leap_counter += 0
    if leap_counter == 1 and month == 2:  # check for february in leap year
        return 29
    if leap_counter == 0 and month == 2:  # check for february in normal year
        return 28
    if month in thirty_days_months:  # check for months with 30 days.
        return 30
    if month in thirty_one_days_months:  # check for months with 31 days.
        return 31


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:  # checks for validity of year
        if 1 <= month <= 12:  # checks for validity of month
            if 1 <= day <= days_in_month(year, month):  # checks for validity of day
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1):  # calls is_valid_date function to check validity of date
        date1 = datetime.date(year1, month1, day1)  # assigning first date to variable date1
        if is_valid_date(year2, month2, day2):  # calls is_valid_date function to check validity of date
            date2 = datetime.date(year2, month2, day2)  # assigning second date to variable date2
            if date1 > date2:
                return 0
            else:
                delta = date2 - date1
                return delta.days
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    if is_valid_date(year, month, day):  # calls is_valid_date function to check validity of date
        todays_date = datetime.date.today()  # assigns today's date to a variable
        date_of_birth = datetime.date(year, month, day)  # assigns given date to a variable
        if date_of_birth > todays_date:
            return 0
        else:
            delta = todays_date - date_of_birth  # doing difference of date to find age in days
            return delta.days
    else:
        return 0
        
        
# submitted by Dhananjay Pratap Lodhi
