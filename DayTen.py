# Function with output or with return value

# def format_name(first_name, last_name):
#     formated_first_name = first_name.title()
#     formated_last_name = last_name.title()
# # to use multiple returns in a single function we use if else statements
#     return f"{formated_first_name} {formated_last_name}"
#
#
# print(format_name('ahmed', 'iqbal'))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    check_leap = is_leap(year)
    if check_leap:
        month_days[1] = 29
        print(month_days)


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days_in_month(year, month)
