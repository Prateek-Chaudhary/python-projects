print("................Body Mass Index Calculator..............")
weight = float(input("Enter your weight in KG\n"))
height = float(input("Enter your height in meter\n"))
BMI = weight/(height**2)
if BMI < 18.5:
    print("Your BMI is :", BMI)
    print('''You are in under weight category\n
        So, you take your proper diet and maintain your Physic...''')
elif BMI >= 18.5 and BMI <= 25:
    print("Your BMI is : ", BMI)
    print("You are in normal weight category\nSo, maintain this category proper..")
else:
    print("Your BMI is : ", BMI)
    print('''You are in over weight category\nYou need weight loss diet''')
