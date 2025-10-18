import smtplib

to = input("Enter Recipient's Email: \n")
content = input("Enter content for Email: \n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()           #starts communication with server
    server.starttls()
    server.login('realgaurav68@gmail.com', 'Gaurav@lu#2344')
    server.sendmail('realgaurav68@gmail.com', to, content)
    server.close()

sendEmail(to, content)