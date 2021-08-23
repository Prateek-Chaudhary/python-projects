name = input("Enter the name\n")
nm = name.split(" ")
ac = " "
for i in nm:
    ac = ac + str(i[0]).upper()
print(ac)
