import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts= ['www.tada1765@gmail.com', 'tohweiquantum@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out this HTML text here!!!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts[0]
# msg['To'] = ', '.join(contacts)
msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
