# Temperature converter
print("Enter the temperature")
print("From which you want to convert:")
temp1 = input()
print("To which temperature:")
temp2 = input()

if temp1 == "celcius":
    celcius = float(input("enter the temperature in celcius :"))
    if temp2 == "fahrenheit":
        f = 9/5*celcius+32
        print("Temperature in Fahrenheit is ", f)
    else:
        k = 273.15+celcius
        print("Temperature in Kelvin is ", k)
elif temp1 == "fahrenheit":
    fahrenheit = float(input("enter the temperature in fahrenheit :"))
    if temp2 == "celcius":
        c = 5/9*(fahrenheit-32)
        print("Temperature in Celcius is ", c)
    else:
        k = 5/9*(fahrenheit-32)+273.15
        print("Temperature in Kelvin is ", k)
else:
    kelvin = float(input("enter the temperature in kelvin :"))
    if temp2 == "celcius":
        c = kelvin-273.15
        print("Temperature in Celcius is ", c)
    else:
        f = 9/5*(kelvin-273.15)+32
        print("Temperature in Fahrenheit is ", f)
