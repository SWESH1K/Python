dates = []
current_dates = []
number_of_days_leap = [0,31,29,31,30,31,30,31,31,30,31,30,31]
number_of_days_nonleap = [0,31,28,31,30,31,30,31,31,30,31,30,31]
final_days = 0
dob_days = 0
cur_days = 0
# Date of Birth
user_input = input("Please enter your date in DOB: ")
dates.append(user_input)
user_input = input("Please enter your month in DOB: ")
dates.append(user_input)
user_input = input("Please enter your year in DOB: ")
dates.append(user_input)
# Current Date
user_input = input("Please enter the date in Today's Date: ")
current_dates.append(user_input)
user_input = input("Please enter the month in Today's Date: ")
current_dates.append(user_input)
user_input = input("Please enter the year in Today's Date: ")
current_dates.append(user_input)
# Printing out the age in years
age_year = int(current_dates[2]) - int(dates[2])
print(f"Your are {age_year} years old.")
# Printing out the age in months
age_month = (age_year*12)+int(current_dates[1])-int(dates[1])
print(f"You are {age_month} months old.")
## Printing out age in Days
class days_counter():
    def __init__(self, type) -> None:
        self.type = type

    def get_date(self):
        days = 0
        run = True
        while run:
            if int(current_dates[1]) > 0:
                days += self.type[int(current_dates[1])]
                current_dates[1] = int(current_dates[1]) - 1
            else:
                #print("The number of days you lived: ", days)
                run = False

run = True
while run:
    # Date of Birth days
    if int(dates[2])/4 == int(dates[2])//4:
        if int(current_dates[1]) > 0:
            dob_days += number_of_days_leap[int(current_dates[1])]
            current_dates[1] = int(current_dates[1]) - 1
        else:
            run = False
    else:
        if int(current_dates[1]) > 0:
            dob_days += number_of_days_nonleap[int(current_dates[1])]
            current_dates[1] = int(current_dates[1]) - 1
        else:
            run = False
    # Current year days
    if int(dates[2])/4 == int(dates[2])//4:
        if int(current_dates[1]) > 0:
            cur_days += number_of_days_leap[int(current_dates[1])]
            current_dates[1] = int(current_dates[1]) - 1
        else:
            cur_days = 366 - cur_days
            run = False
    else:
        if int(current_dates[1]) > 0:
            cur_days += number_of_days_nonleap[int(current_dates[1])]
            current_dates[1] = int(current_dates[1]) - 1
        else:
            cur_days = 365 - cur_days
            run = False
# For whole years
run = True
while run:
    if int(dates[2]) < int(current_dates[2]):
        if int(dates[2])/4 == int(dates[2])//4:
            final_days += 366
            dates[2] = int(dates[2]) + 1
        else:
            final_days += 365
            dates[2] = int(dates[2]) + 1
    else:
        run = False

total_final_days = final_days - (cur_days + dob_days) - (int(dates[0]) + (number_of_days_leap[int(current_dates[1])] - int(current_dates[0])))
print(f"The number of days: {total_final_days}")