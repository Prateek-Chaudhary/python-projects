# This is a snake water gun game
import random
g = 0
comp = 0
ls = ['snake', 'water', 'gun']
c = random.choice(ls)
i = 1
while i <= 5:
    gamer = input("Enter your choice\n1.snake 2.water 3. gun\n")
    if gamer == 'snake' and c == 'water':
        g += 1
        print("Gamer win this chance")
    elif gamer == 'snake' and c == 'gun':
        comp += 1
        print("Computer win this chance")
    elif gamer == 'water' and c == 'snake':
        comp += 1
        print("Computer win this chance")
    elif gamer == 'water' and c == 'gun':
        g += 1
        print("Gamer win this chance")
    elif gamer == 'gun' and c == 'snake':
        g += 1
        print("Gamer win this chance")
    elif gamer == 'gun' and c == 'water':
        comp += 1
        print("Computer win this chance")
    elif gamer == c:
        print("Tie")
    else:
        print("something is wrong")

    i = i + 1

if g < comp:
    print("Computer win this match")
    print("Computer score is :", comp)
    print("Your score is :", g)
else:
    print("You win this match")
    print("Your score is :", g)
    print("Computer score is :", comp)
