# WHEN USER ENTERS A YEAR, THE CODE DETECTS IF ITS LEAP YEAR OR NOT.

# LEAP YEAR DIVISIBLE BY 4, EXCEPT CENTURY YEARS (1500,1900 etc...)
# CENTURY YEAR IS LEAP YEAR, IF ITS DIVISIBLE BY 400.

#o(1)
def leapyear(year):
    if year % 4 == 0:                    # If year divisible by 4 with no remainder
        if year % 100 == 0:                 # If year divisible by 100 with no remainder
            if year % 400 == 0:                # If year divisible by 400 with no remainder
                print(f'{year} is leap year!')
            else:
                print(f'{year} is NOT leap year!')      # if not divisible by 400, then not leap year.
        else:
            print(f'{year} is leap year')           # if not divisible by 100, then leap year.
    else:
        print(f'{year} is NOT leap year!')      # If not divisible by 4, then not leap year.

leapyear(2000) # leap year
leapyear(2012) # leap year
leapyear(1900) # not a leap year
leapyear(2022) # not a leap year


