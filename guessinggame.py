print("-------------------Guessing game---------------------")
import random
while True:
    rd = random.randint(0, 9)
    print("Computer guess a number\nNow its your turn")
    n = int(input("guess any number and write\n"))
    if rd == n:
        print("generated number is : ", rd)
        print("Your number is : ", n, end=" -- ")
        print("WOW your guess is correct")
    else:
        print("generated number is : ", rd)
        print("your number is : ", n)
        print("Better luck  next time")
    print("------------------Want to play again---------------------")
    w= int(input("1-Yes\n 2-No\n"))
    if w == 1:
        continue
    else:
        break