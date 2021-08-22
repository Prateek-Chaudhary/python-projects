import smtplib

sender = "prateek.pc07@gmail.com"
reciever = "prateek.pc07@outlook.com"
msg = "This is a message for you about reminding that you did not submit your work."

try:
    pasword = input("Enter your gmail password")
    obj = smtplib.SMTP("gmail.com", 587)
    obj.login(sender, pasword)
    obj.sendmail(sender, reciever, msg)

    print("Email is successfully sent")

except Exception as e:
    print(e)
    print("The email is not sent")
