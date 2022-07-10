# Estimate monthly expense based on current spending behavior.
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


