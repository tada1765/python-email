import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Staturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'www.tada1765@gmail.com', msg)
