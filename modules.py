# Organize functions and classes here

from cgi import test
from datetime import datetime
from datetime import date
import math
from sqlite3 import Time
import time
from xml.dom import pulldom

from more_itertools import time_limited



class Time_Estimator:


    # Calculate current spot of the month based on current time for more accurate estimation
    # 30 days has September,
    # April, June, and November.
    # When short February's done
    # All the rest have 31...
    # leap year = 00, 04, 08, 12, 16, 20, 24, 28, 32, 36, 40 .... so on
    # leap year calculation: 
    # if the year can be divided by 4, then it is a leap year, use math.remainder to check leap year.

    current = datetime.now()
    month_output = int(current.strftime("%m"))
    year_output = int(current.strftime("%y"))
    day_output = int(current.strftime("%d"))


    def leap_year(year_output):

            year = year_output
            remainder = math.remainder(year, 4)

            if remainder != 0:
                Leap_Year = False

            else:
                Leap_Year = True

            return Leap_Year

    
    Leap_Year = leap_year(year_output)


    def days_left(Leap_Year, month_output, day_output):

        short_month = [4, 6, 9, 11]

        if Leap_Year == True and month_output == 2:
            remaining_days = 29 - day_output

        elif Leap_Year == False and month_output == 2:
            remaining_days = 28 - day_output

        elif Leap_Year == True and month_output in short_month == True:
            remaining_days = 30 - day_output

        else:
            remaining_days = 31 - day_output

        return remaining_days

    remaining_days = days_left(Leap_Year, month_output, day_output)

    def days_in_month(Leap_Year, month_output):

        short_month = [4, 6, 9, 11]

        if Leap_Year == True and month_output == 2:
            days_in_month = 29 

        elif Leap_Year == False and month_output == 2:
            days_in_month = 28

        elif Leap_Year == True and month_output in short_month == True:
            days_in_month = 30

        else:
            days_in_month = 31

        return days_in_month

    total_days = days_in_month(Leap_Year, month_output)


class calculate:


    def estimate_expense():

        # Input variables
        # food = int(input("How much did you spend on your most recent food/drink? "))
        # gas = int(input("How far did you drive the last time you used your car? "))
        # gas_mpg = int(input("What's your car's gas mileage? "))
        # misc = int(input("How much did you spend on your last non-essential items? "))
        # misc_freq = int(input("How many times did you spend money on non-essentials so far this month? "))
        # payment = int(input("How much is your recurring payment this month? "))

        # Test input variables, test the code without having to do input on every trial, comment it to switch to the real code.
        food = 15
        gas = 10
        gas_mpg = 18
        misc = 20
        misc_freq = 4
        payment = 1000

        # Formulas
        food_expense = food * Time_Estimator.total_days
        gas_expense = (gas / gas_mpg) * 5.21 * Time_Estimator.total_days
        misc_expense = (Time_Estimator.total_days / misc_freq) * misc
        total_expense = food_expense + gas_expense + misc_expense + payment

        print("Your monthly estimated expense so far is",total_expense,"dollars!!")

        upcoming_days = Time_Estimator.remaining_days
        past_days = Time_Estimator.total_days - Time_Estimator.remaining_days
        reduce_by_20_percent = 0.8
        reduce_by_half = 0.5
        gas_prices = 5.21

        # Formulas
        food_saving = (food * reduce_by_20_percent) * upcoming_days + (food * past_days)
        gas_saving = ((gas / gas_mpg) * gas_prices * (upcoming_days * reduce_by_half)) + ((gas / gas_mpg) * gas_prices * past_days)
        misc_saving = misc_freq * misc
        all_save = food_saving + gas_saving + misc_saving + payment
        no_save_gas = food_saving + misc_saving + payment
        no_save_misc = food_saving + gas_saving + payment
        no_save_food = gas_saving + misc_saving + payment
        only_food = food_saving + payment
        only_gas = gas_saving + payment
        only_misc = misc_saving + payment

        # Input variables
        save_food = input("Can you reduce your food spending by 20 percent starting now? y / n ")
        save_gas = input("Can you reduce the days you use cars by 50 percent starting now? y / n ")
        save_misc = input("Can you stop buying non-essential things starting now? y / n ")

        if (save_food or save_gas or save_misc) and not (save_food and save_gas and save_misc) == "y" or "Y":

            condition = [save_food, save_gas, save_misc]
            
            if condition == ["y","y","y"]:
                print("Your new estimated expense after saving is",all_save,"dollars! Good job!!")
            elif condition == ["n","n","n"]:
                print("You didn't save anything!!")
            elif condition == ["y","y","n"]:
                print("Your new estimated expense after saving is",no_save_misc,"dollars!")
            elif condition == ["y","n","y"]:
                print("Your new estimated expense after saving is",no_save_gas,"dollars!")
            elif condition == ["n","y","y"]:
                print("Your new estimated expense after saving is",no_save_food,"dollars")
            elif condition == ["y","n","n"]:
                print("Your new estimated expense after saving is",only_food,"dollars!")
            elif condition == ["n","y","n"]:
                print("Your new estimated expense after saving is",only_gas,"dollars!")
            elif condition == ["n","n","y"]:
                print("Your new estimated expense after saving is",only_misc,"dollars!")
            else:
                print("Incorrect input!!!")


            