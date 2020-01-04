import smtplib, ssl
import os


def send_email(message):
    sender_email_address = os.getenv("EMAIL_ADDRESS")
    sender_email_password = os.getenv("EMAIL_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        try:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender_email_address, sender_email_password)
            s.sendmail(sender_email_address, "andrea.santarl@gmail.com", message)
        except smtplib.SMTPAuthenticationError as e:
            print(e)



