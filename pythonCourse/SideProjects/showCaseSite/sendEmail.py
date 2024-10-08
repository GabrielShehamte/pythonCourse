import smtplib, ssl, certifi

host = "smtp.gmail.com"
port = 465

username = "Gabriel.shehamte@gmail.com"
password = "ggll nglg cdiu cjxf"

receiver = "gabebrown012@gmail.com"
context = ssl.create_default_context(cafile=certifi.where())

message = "Testing"

with smtplib.SMTP_SSL(host, port, context=context) as server :
    server.login(username,password)
    server.sendmail(username,receiver,message)