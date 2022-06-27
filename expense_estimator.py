# Estimate monthly expense based on daily spending

print("Welcome to the monthly expense estimator!")
print("I will use your daily expense to estimate your monthly expense.")


def expenses():

    food = int(input("How much did you spend on food and drinks today? "))
    gas_km = int(input("Approximately how far did you travel in km by car today? "))
    utilities = int(input("How much do you have to pay for utilities? "))
    misc = int(input("How much did you spend on other stuff? "))
    payment = int(input("How much is your recurring monthly payment? "))

    gas_calculate = (gas_km/7.6)*30.4 #calculate gas cost based on km/L on a 18mpg car
                                      # 1 gallon = 3.8L, 1 mile = 1.6km
                                      # 1.6km = 3.8L, 1km = 2.375 L
                                      # set the car to 18 mile per gallon, which is 28.8 km per 3.8 Liter
                                      # which means 1 Liter will yield 7.6km of travel distance
                                      # 7.6:1 = 7:x, 7.6x = 7, x = 7/7.6

    monthly_total = food*30 + gas_calculate*30 + misc*30 + payment + utilities
    return monthly_total, food, gas_km, utilities, misc, payment, gas_calculate


expense_total = expenses()


print("Your estimated monthly expense based on your current spending habit is: ",expense_total[0])
print("Now let's see how much you can save by changing your spending behaviors....")


def saving():

    food_save = input("Can you reduce your food cost by 10% tomorrow? y/n ")
    gas_km_save = int(input("How many days can you reduce from driving? "))
    food_calc = expense_total[1]*0.1*30-expense_total[1]
    gas_calc = (expense_total[6]*30) - (expense_total[6]*(30-gas_km_save))

    return food_calc, gas_calc, food_save, gas_km_save


savings = saving()


if savings[2] == "y" or "Y":
    if savings[3] > 0:
        print("You will save ", savings[0], "on food")
        print("You will save ",savings[1], "on gas")
    else:
        print("You will save ", savings[0], "on food")
elif savings[2] == "n" or "N":
    if savings[3] > 0:
        print("You will save ", savings[1], "on gas")
    else:
        print("You will not save any money!!")