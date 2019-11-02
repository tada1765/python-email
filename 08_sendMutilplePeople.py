import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts= ['www.tada1765@gmail.com', 'tohweiquantum@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out this PDF here!!!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
# msg['To'] = ', '.join(contacts)
msg.set_content('PDF attached...')

files = ['Black logo_TAR UC copy.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet_stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
