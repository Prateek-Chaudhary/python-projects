my_number = 7
for i in range(1, 6):
    ur_number = int(input("enter your number bw 1 to 10\n"))
    if ur_number < my_number:
        print("try bigger number\n")
    elif ur_number > my_number:
        print("try smaller number\n")
    elif my_number == ur_number:
        print("WOW! You win\n")
        print("correct guess in :", i,"chance")
        break
    else:
        print("Wrong thing entered")
    if i == 5:
        print("Game Over\n")
        print("Your chances are over\n")
    c = 5-i
    print("chance remaining :", c)