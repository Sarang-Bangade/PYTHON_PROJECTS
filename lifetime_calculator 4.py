
# live Lifetime Calculator.

def calcualte_minutes (age_years):
    DAYS_IN_YEAR = 365.5
    HOURS_IN_DAY =24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    return round (total_days), round(total_hours), round(total_minutes)

while True:
    try:
        age = float(input("Enter your age in Years"))
        days, hours, minutes = calcualte_minutes(age)

        print("\n You are approximately:")
        print(f"  - {days} days old")
        print(f"  -  {hours} hours old")
        print(f"  - {minutes} minutes old\n")

        again = input("Would you like to try again? (y/n)").strip().lower()

        if again != 'y':
            print("Good Bye and visit next time")
            break
    except :
        print("Sorry! plz enter a valid number")
