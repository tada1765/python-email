# python-email
reference: from Corey Schafer.

reference: How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More from Corey Schafer [video here](https://www.youtube.com/watch?v=JRCJ6RtE3xU)

1.) Google account setting.
---- 
Google Account Settings:
https://myaccount.google.com/lesssecureapps
https://myaccount.google.com/apppasswords?rapt=AEjHL4MPx6tW8MY5-Ak8UXTgmej5h7RIhxYRcBK00cm_nrQbPbmBMyGyVt4avH7oZUjk7wKXzOyrObyJCuYn2sQReXWSjbSaZw

2.) Hide password using OS environment.
---------------------------------------------
win + search environment:...

3.) Create a new project
-----------------------
refer: my open Vision Studio Code project with Virtual environment [detail here](https://trello.com/c/NRmiQf63/8-my-open-vision-studio-code-project-with-virtual-environment)

do not name your file as email.py, because other package of module has use the name, so to prevent crush use other name like mailDemo.py.

4.) Python-email code
--------------------------
on 01_mailDemo.py:

```

import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

print(EMAIL_PASSWORD)
print(EMAIL_ADDRESS)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Staturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'xxxxxxxxxxxx@gmail.com', msg)

```

**result: **
![mailreceived](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/f22099269065d9a6330dafbe31d11b0d/image.png)


5.) local debug server
---------------------------
 start debug mail server on localhost:
goto terminal tpye:
python -m smtpd -c DebuggingServer -n localhost:1025

create new python file 02_localhostDebug.py:

```

import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Staturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'xxxxxxxxxxx@gmail.com', msg)

```

**result: on the terminal will show:**
![localhost](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/5c62236c76233c13fabb3f5bc1ce2e48/image.png)

6.) SMTP SSL
-------------------

create a python file 03_smtpSSL.py:

```

import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Staturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'xxxxxxxxxxxx@gmail.com', msg)

```

**same result on 1.)**

7.) use email.message package for proper subject and email format:
--------------------

create 04_UseSendMessage.py file:

```

import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'xxxxxxxxxxx@gmail.com'
msg.set_content('How about dinner at 6pm this Staturday?')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


```

**result : same as 1.)**

8.) email attachment
--------------------

create a python file 05_emailAttachment.py:

```

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out this image here!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'xxxxxxxxxxxx@gmail.com'
msg.set_content('Image attached...')

with open('pic.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    # print(file_type)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

```

**result:**
![attachment](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/c4481c19169d376771a064f8fa2c33a7/image.png)

9.) attach multiple image
--------------------------

create a python file 06_multipleAttachment.py

```

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out this image here!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'www.tada1765@gmail.com'
msg.set_content('Image attached...')

files = ['pic.jpg', 'default.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

```

![mutiAttach](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/24d62cf891fea74c1bec585feeef710f/image.png)

10.) PDF as attachment email send
----------------------

create a python file 07_PDFAttach.py:

```

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out this PDF here!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'xxxxxxx@gmail.com'
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

```

![PDF](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/32e671c3f7d9e372e39536d405d6164c/image.png)

11.) send to multiple people.
--------------------
create a python file 08_sendMutilplePeople.py:

```

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts= ['xxxxxxxxxxxx@gmail.com', 'yyyyyyyyyyyyyy@gmail.com']

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

```

**result:[bothreceive]**

12. Create HTML messages email
----------------
create a python file 09_HTMLMessage.py:

```

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts= ['xxx@gmail.com', 'yyyy@gmail.com']

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


```

""" = multi-line string

**result:**
![HTMLMSG](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5dbbf8043753ca650f974196/83fc987e853eea571380dce8151b825c/image.png)


