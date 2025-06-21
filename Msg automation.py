import getpass
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


Gmail_user = input("Gmail User:")
print("prompting for app specific password")
GMAIL_PASSWORD = getpass.getpass("App Specific password:")

msg = MIMEMultipart('mixed')
msg["From"] = Gmail_user
msg["To"] = input("Email To:")
msg['subject'] = input("Subject:")
msg.attach(MIMEText( input('Enter the content:'),"plain"))

filename = "file.txt.jpeg" # Add file from your directory here
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(Gmail_user,GMAIL_PASSWORD)
        smtp.send_message(msg)
    print("Email sent successfully")
except Exception as e:
    print(f"Error sending email : {e}")

