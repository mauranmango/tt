import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


def send_email(subject, sender, recipients, text_body, html_body):
    """
    Helper function that send email
    :param subject:
    :param sender:
    :param recipients:
    :param text_body:
    :param html_body:
    :return:
    """
    msg = MIMEText(f'{text_body}', 'plain', 'utf-8')
    msg['Subject'] = Header(f'{subject}', 'utf-8')
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    server = smtplib.SMTP(host='smtp.mail.yahoo.com', port=587, timeout=10)
    server.set_debuglevel(1)
    try:
        server.starttls()
        server.login(user=sender, password=os.environ.get('MAIL_PASSWORD'))
        server.sendmail(from_addr=sender, to_addrs=recipients, msg=msg.as_string())
    finally:
        server.quit()
