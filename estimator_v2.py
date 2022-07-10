# Estimate monthly expense based on current spending behavior.
# Added datetime function to calculate the total day of the current month adjusted by leap year, long month, short month, long february and short feburary.
# The program will take into consideration the current day of the month
# Then it will estimate the expense done so far, and then add it to the remainder days of the month.
# Example : today is 7/10, there are 31 days in july, so there will be 21 day remaining.
#           the program will estimate the 10 day expense based on current behavior
#           once the user input a new behavior by accepting the new money saving strategy
#           the program will then calculate a new estimate based on the adjusted action
#           and then added the new calculation with the already spent days to come up with new total
#           (10 days old estimate) + (21 days adjusted estimate) = new adjusted monthly expense estimate

from modules import  calculate
import time

wait = time.sleep(2)

def main():

    print("Hello, welcome to the expense estimator version 2.0")
    wait
    print("I will calculate your estimated monthly expense based on your current spending behavior.")
    wait
    calculate.estimate_expense()


main()


