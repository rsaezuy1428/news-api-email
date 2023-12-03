import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "rafaelsaez1428@gmail.com"
    password = "fjmo pvaf dhix dsjg"

    receiver = "rafaelsaez1428@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
