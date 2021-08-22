import datetime

print("Health Management System")


def rohanwrite():
    def rdiet():
        with open("rdiet.txt", "a") as rd:
            date = datetime.datetime.now()
            dt = input("Enter your food -\t")
            dd = str(date) + "\t" + dt + "\n"
            rd.write(dd)

    def rexercise():
        with open("rexercise.txt", "a") as re:
            edate = datetime.datetime.now()
            edt = input("Enter your exercise -\t")
            edd = str(edate) + "\t" + edt + "\n"
            re.write(edd)

    c1 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if c1 == 1:
        rdiet()
    elif c1 == 2:
        rexercise()
    else:
        print("Not right choise")


def rohanread():
    def rdiet():
        with open("rdiet.txt", "r") as rd:
            opr = rd.read()
            print(opr)

    def rexercise():
        with open("rexercise.txt", "r") as re:
            ope = re.read()
            print(ope)

    cc1 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if cc1 == 1:
        rdiet()
    elif cc1 == 2:
        rexercise()
    else:
        print("Not right choise")


def vikaswrite():
    def vdiet():
        with open("vdiet.txt", "a") as vd:
            date2 = datetime.datetime.now()
            dt2 = input("Enter your food -\t")
            dd2 = str(date2) + "\t" + dt2 + "\n"
            vd.write(dd2)

    def vexercise():
        with open("vexercise.txt", "a") as ve:
            edate2 = datetime.datetime.now()
            edt2 = input("Enter your exercise -\t")
            edd2 = str(edate2) + "\t" + edt2 + "\n"
            ve.write(edd2)

    c2 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if c2 == 1:
        vdiet()
    elif c2 == 2:
        vexercise()
    else:
        print("Not right choise")


def vikasread():
    def vdiet():
        with open("vdiet.txt", "r") as vd:
            opr2 = vd.read()
            print(opr2)

    def vexercise():
        with open("vexercise.txt", "r") as ve:
            ope2 = ve.read()
            print(ope2)

    cc2 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if cc2 == 1:
        vdiet()
    elif cc2 == 2:
        vexercise()
    else:
        print("Not right choise")


def sanamwrite():
    def sdiet():
        with open("sdiet.txt", "a") as sd:
            date3 = datetime.datetime.now()
            dt3 = input("Enter your food - \t")
            dd3 = str(date3) + "\t" + dt3 + "\n"
            sd.write(dd3)

    def sexercise():
        with open("rexercise.txt", "a") as se:
            edate3 = datetime.datetime.now()
            edt3 = input("Enter your exercise -\t")
            edd3 = str(edate3) + "\t" + edt3 + "\n"
            se.write(edd3)

    c3 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if c3 == 1:
        sdiet()
    elif c3 == 2:
        sexercise()
    else:
        print("Not right choise")


def sanamread():
    def sdiet():
        with open("sdiet.txt", "r") as sd:
            opr3 = sd.read()
            print(opr3)

    def sexercise():
        with open("sexercise.txt", "r") as se:
            ope3 = se.read()
            print(ope3)

    cc3 = int(input("Choose option\n1- Diet\n2- Exercise\n"))
    if cc3 == 1:
        sdiet()
    elif cc3 == 2:
        sexercise()
    else:
        print("Not right choise")


while True:
    cl_names = int(input("Choose client -\n1- Rohan\n2- Vikas\n3- Sanam\n"))
    if cl_names == 1:
        wc1 = int(input("What do you want\n1- Write Data\n2- Retrieve Data\n"))
        if wc1 == 1:
            rohanwrite()
        elif wc1 == 2:
            rohanread()
        else:
            print("Entered wrong input")
    elif cl_names == 2:
        wc2 = int(input("What do you want\n1- Write Data\n2- Retrieve Data\n"))
        if wc2 == 1:
            vikaswrite()
        elif wc2 == 2:
            vikasread()
        else:
            print("Entered wrong input")
    elif cl_names == 3:
        wc3 = int(input("What do you want\n1- Write Data\n2- Retrieve Data\n"))
        if wc3 == 1:
            sanamwrite()
        elif wc3 == 2:
            sanamread()
        else:
            print("Entered wrong input")
    else:
        print("Sorry, Client not available")

    tr = int(input("Do you want to Write or Retrieve Data again\n1- Yes\n2-No\n"))
    if tr == 1:
        continue
    else:
        break
