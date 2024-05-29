import math


def day_of_week(day, month, year):
    h = (day + math.floor((13*month + 13)/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) % 7
    return (h+5)%7 + 1
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def month_num(month_name):
    if month_name == "January":
        return 1
    elif month_name == "February":
        return 2
    elif month_name == "March":
        return 3
    elif month_name == "April":
        return 4
    elif month_name == "May":
        return 5
    elif month_name == "June":
        return 6
    elif month_name == "July":
        return 7
    elif month_name == "August":
        return 8
    elif month_name == "September":
        return 9
    elif month_name == "October":
        return 10
    elif month_name == "November":
        return 11
    elif month_name == "December":
        return 12

def num_days_in(month_num, year):
    if month_num == 2:
        if is_leap(year):
            return 29
        else:
            return 28
        #These are the only motnhs left
    elif month_num in [4, 6, 9, 11]:
        return 30
    else:
        return 31



def num_weeks(month_num, year):
    days_in_month = num_days_in(month_num, year)
    num_weeks = days_in_month // 7  # Integer division to get the number of full weeks
    if days_in_month % 7 != 0:
        num_weeks += 1  # If there are remaining days, add an extra week
    return num_weeks



def week(week_num, start_day, days_in_month):
    output = ""
    if week_num== 1:
        output += "  " * start_day
    # will start by handling the first week cases (Where the first week's output will have spaces)
    start_of_week = (1 + (7 - start_day) + 1                                                                                                                                                                                                                                                                                                                              ) + (week_num - 2) * 7

    for i in range(start_of_week, start_of_week + 7):
        if(i<0):
            continue
        else:
            if(i < 10):
                output += " " + str(i) + " "
            else:
                output += str(i) + " "
    return output
def main():
    month_word = input("Enter month:\n")
    month = month_num(month_word)

    year = eval(input("Enter year:\n"))
    #returns the firss
    starting_day = day_of_week(1,month,year)
    days_in_month = num_days_in(month,year)

    print(month_word)
    print("Mo Tu We Th Fr Sa Su")

    for i in range(1,num_weeks(month,year) + 1):
        print(week(i,starting_day,days_in_month))


if __name__=='__main__':
    main()






