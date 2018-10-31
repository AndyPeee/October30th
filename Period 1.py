def product(number_1):
    number_2=input("What number would you like? ")
    sum=int(number_1)+(int(number_2))
    print (sum)
def same(number_3):
    number_4=input("What number would you like? ")
    if number_3==number_4:
        print("TRUE")
    else:
        print("FALSE")
import math
def quick_pythagoras():
    a = input("A value ")
    b = input("B value ")
    a = int(a) * int(a)
    b = int(b) * int(b)
    c = int(b) + int(a)
    c = math.sqrt(c)
    print("Your hypotenuse is: " + str(c))
def tip_calculator():
    cost = input("What is the price? ")  # first lines take and store inputs
    tip = input("What percent would you like to tip? ")
    tip = int(tip) / 100
    totaltip = tip * int(cost)
    print("Your tip is")
    print(totaltip)
    totalcost = int(totaltip) + int(cost)
    print("Your final price is")
    print(totalcost)
def temperature_converter():
    ctof = input("Would you like to convert from Celsius to Fahrenheit? (yes or no)")
    if ctof == ("yes"):
        cx = input("What is your Celsius value? ")
        fx = int(cx) * 1.8
        fx = int(fx) + 32
        print("Your Fahrenheit value is")
        print(fx)
    if ctof == ("no"):
        ftoc = input("Would you like to convert Fahrenheit to Celsius? (yes or no)")
        if ftoc == ("yes"):
            fy = input("What is your Fahrenheit value? ")
            cy = int(fy) - 32
            cy = int(cy) / 1.8
            print("Your Celsius value is")
            print(cy)
        if ftoc == ("no"):
            print(
                "Wait, why are you even here then?")
def letters(string):
    letter=input("What letter do you want? ")
    if letter in string:
        print("TRUE")
    else:
        print("FALSE")
r=1
while r==1:
    mode=input("What mode do you want? ")
    if mode == ("product"):
        product(number_1 = input("What number do you want? "))
    if mode == ("same"):
        same(number_3 = input("What number do you want? "))
    if mode==("quick pythagoras"):
        quick_pythagoras()
    if mode == ("tip calculator"):
        tip_calculator()
    if mode==("temperature converter"):
        temperature_converter()
    if mode==("string"):
        letters(string=input("What sentence are you looking for? "))
    if mode == ("leave"):
        exit(code="thanks for coming")