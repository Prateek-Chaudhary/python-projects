fortune = {
"1":"You will find a bushel of money.",
"2": "Your smile will tell you what makes you feel good.",
"3": "You are going to have some new clothes.",
"4": "Your family is young, gifted and attractive.",
"5": "There is a true and sincere friendship between you both.",
"6": "A smiling stranger will bring you some troubling news.",
"7": "Face facts with dignity.",
"8": "You are magnetic in your bearing.",
"9": "You are free to invent your life.",
"10": "Good sense is the master of human life.",
"11": "If winter comes, can spring be far behind.?",
"12": "Change is certain, be accepting.",
"13": "If you don't have time to live your life now, when will you?",
"14": "Ignorance never settles a question.",
"15": "The best year-round temperature is a warm heart and a cool head.",
"16": "Avert misunderstanding by calm, poise, and balance.",
"17": "Simplicity and clarity should be your theme in dress.",
"18": "You have a potential urge and the ability for accomplishment.",
"19": "Do you believe? Endurance and persistence will be rewarded.",
"20": "Good Luck bestows upon you. You will get what your heart desires.",
"21": "Pat yourself on the back for creating an opportunity.",
"22": "It could be better, but it's good enough.",
"23": "You will find a thing. It may be important.",
"24": "The calling that has sounded will not be the lasting call.",
"25": "In youth and beauty, wisdom is rare.",
"26": "The sage acts by doing nothing.",
"27": "Move carefully, as when crossing a river in winter.",
"28":"When tempers flare up in the family, too great severity brings remorse.",
}
import random
rd = random.randint(0, 27)
fr = list(fortune.keys())
while True:
    horo = input("enter your horoscope")
    if horo == "aquarius":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "pisces":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "aries":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "taurus":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "gemini":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "cancer":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "leo":
        print("fortune is :")
        print(fortune[fr[rd]])
    elif horo == "virgo":
        print("fortune is :")
        print(fortune[fr[rd]])
    else:
        print("XXXXX --- Invalid Input --- XXXXX")
    print("Do you want to Use again")
    n = int(input("1 - Yes\n 2 - No\n"))
    if n == 1:
        continue
    else:
        break
