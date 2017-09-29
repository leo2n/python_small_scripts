"""
Calculate how long the days you lived
Writed by leo
2017-09-28
"""
from datetime import date


# get NOW year, month, day
NOW = date.today()
TODAY_YEAR = NOW.year
TODAY_MONTH = NOW.month
TODAY_DAY = NOW.day
TODAY_LIST = [TODAY_YEAR, TODAY_MONTH, TODAY_DAY]

# get BORN year, month, day
BORN_YEAR, BORN_MONTH, BORN_DAY = input("Please input\
 your born year, month, day: (split by one space)").split(" ")
BORN_YEAR = int(BORN_YEAR)
BORN_MONTH = int(BORN_MONTH)
BORN_DAY = int(BORN_DAY)
BORN_LIST = [BORN_YEAR, BORN_MONTH, BORN_DAY]

RENNIAN = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NOT_RENNIAN = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_rennian(year):
    """
    year: int
    return: True or False
    """
    flag = False
    if year%100 == 0 and year%400 == 0:
        flag = True
    elif year%100 != 0 and year%4 == 0:
        flag = True
    else:
        flag = False
    return flag

def is_input_vaild(born, today):
    """
    born: int[]
    today: int[]
    Just check if input date is earlier than today
    """
    flag = True
    if int(str(born[0]+str(born[1])+str(born[2]))) > int(str(today[0]+str(today[1])+str(today[2]))):
        flag = False
    else:
        flag = True
    return flag

def day_count1():
    """
    count day(BORN_YEAR, TODAY_YEAR)
    return day_count1: int
    """
    count1 = 0
    for year in range(BORN_YEAR+1, TODAY_YEAR):
        if is_rennian(year) is True:
            count1 += 366
        elif is_rennian(year) is False:
            count1 += 365
    return count1

def day_count2():
    """
    count day(., BORN_YEAR]
    count2: int
    """
    count2 = 0
    if is_rennian(BORN_YEAR) is True:
        for month_index in range(1, BORN_MONTH):
            count2 += RENNIAN[month_index]
        count2 += BORN_DAY
        count2 = 366 - count2
    elif is_rennian(BORN_YEAR) is False:
        for month_index in range(1, BORN_MONTH):
            count2 += NOT_RENNIAN[month_index]
        count2 += BORN_DAY
        count2 = 365 - count2
    return count2

def day_count3():
    """
    count day[TODAY_YEAR, .]
    """
    count3 = 0
    if is_rennian(TODAY_YEAR) is True:
        for month_index in range(1, TODAY_MONTH):
            count3 += RENNIAN[month_index]
        count3 += TODAY_DAY
    elif is_rennian(TODAY_YEAR) is False:
        for month_index in range(1, TODAY_MONTH):
            count3 += NOT_RENNIAN[month_index]
        count3 += TODAY_DAY
    return count3

def gap():
    """
    Calculate gap between BORN and TODAY
    gap_days: datetime.timedelta
    gap_date: datetime.date
    gap based on date(1,1,1)
    """
    gap_days = date.today() - date(BORN_YEAR, BORN_MONTH, BORN_DAY)
    gap_days = date(1, 1, 1) + gap_days
    gap_date = date(gap_days.year-1, gap_days.month-1, gap_days.day-1)
    return gap_date

def main():
    """
    Calculate and display the result
    """
    allday = day_count1() + day_count2() + day_count3()
    print("Hello, Calculating your living day, wait for a second : )")
    print("You have lived for {} days".format(allday))
    print("You have lived for {} years, {} months,\
{} days".format(gap().year, gap().month, gap().day))

if __name__ == "__main__":
    main()
