#! /usr/bin/python3
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText
SMTP_Host = 'imap-mail.outlook.com'
sender = 'njahirhardy@hotmail.com'
receivers = ['pvn10092001vn@gmail.com']
username = "njahirhardy@hotmail.com"
password = "Dayanna"
# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'
content = """\
Test SMTTP Python script
"""
subject = "Sent from vinasupport.com"
try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender  # some SMTP servers will do this automatically, not all
    conn = SMTP(SMTP_Host)
    conn.set_debuglevel(False)
    conn.login(username, password)
    try:
        conn.sendmail(sender, receivers, msg.as_string())
    finally:
        conn.quit()
except Exception as error:
    print(error)
