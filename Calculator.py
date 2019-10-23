from math import*
import math
def prog():
    print(("Hello, welcome to Python Caculator Early Access v1.12").center(100))
    print(("="*56).center(100))
    fnum = float(input("Please insert the first number: "))
    userinput = input("Please insert which opreation you would like to use by using the number next to it: \n1.Addtion\n2.Subtraction\n3.Mutiplication\n4.Division\n5.Pi\n6.Square Root\n")
    if userinput == "1":
        l1num = float(input("Please insert the second number "))
        print("Anwser:",fnum+l1num)
    elif userinput == "2":
        l2num = float(input("Please insert the second number "))
        print("Anwser:",fnum-l2num)
    elif userinput == "3":
        l3num = float(input("Please insert the second number "))
        print("Anwser:",fnum*l3num)
    elif userinput == "4":
        l4num = float(input("Please insert the second number "))
        if l4num == 0:
            print("You broke the calculator")
            exit()
        print("Anwser:",fnum/l4num)
    elif userinput == "5":
        print(math.pi*fnum)
    elif userinput == "6":
        print(math.sqrt(fnum))
    elif userinput == "DOOT":
        print("*"*3," "*2,"*"*4, " ","*"*4, " ","*"*3)
        print("*  *", " ","*  *"," ", "*  *","   *")
        print("*  *", " ","*  *"," ", "*  *","   *")
        print("*  *", " ","*  *"," ", "*  *","   *")
        print("*  *", " ","*  *"," ", "*  *","   *")
        print("*  *", " ","*  *"," ", "*  *","   *")
        print("*"*3," "*2,"*"*4, " ","*"*4, " "," *")
    else:
        print("You broke the calculator")
prog()
endChoice = input("Do you want to use this program again 1.Yes 2. No")
if endChoice == "1": prog()
else: exit()