import random

elements = ["Scissor", "Paper", "Stone"]
op = random.choice(elements)
while True:
    op_points = 0
    your_points = 0
    for i in range(1, 6):
        you = int(input("Your Choice-\n1. Scissor\n2. Paper\n3. Stone\n"))
        if you == 1:
            if op == "Paper":
                your_points += 1
                print("You Win this chance")
            elif op == "Stone":
                op_points += 1
                print("Opponent Win this chance")
            else:
                print("No one Win this chance")
        elif you == 2:
            if op == "Stone":
                your_points += 1
                print("You Win this chance")
            elif op == "Scissor":
                op_points += 1
                print("Opponent Win this chance")
            else:
                print("No one Win this chance")
        elif you == 3:
            if op == "Scissor":
                your_points += 1
                print("You Win this chance")
            elif op == "Paper":
                op_points += 1
                print("Opponent Win this chance")
            else:
                print("No one Win this chance")
        else:
            print("You give wrong input\nTry again")
            continue
    if op_points > your_points:
        print(f"You LOOSE this game\nYour score {your_points}\nOpponent score {op_points}")
    elif your_points > op_points:
        print(f"You WIN this game\nYour score {your_points}\nOpponent score {op_points}")
    else:
        print("Game Over  No one Win")
     
    ap = int(input("Want to play again\n1. Yes\n2. No\n"))
    if ap == 1:
        continue
    elif ap == 2:
        break
    else:
        print("Wrong attempt")
