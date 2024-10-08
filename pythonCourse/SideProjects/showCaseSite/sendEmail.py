import smtplib, ssl, certifi

def sendEmail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "Gabriel.shehamte@gmail.com"
    password = "ggll nglg cdiu cjxf"

    receiver = "gabriel.shehamte@gmail.com"
    context = ssl.create_default_context(cafile=certifi.where())


    with smtplib.SMTP_SSL(host, port, context=context) as server :
        server.login(username,password)
        server.sendmail(username,receiver,message)