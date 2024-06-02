import smtplib
from email import encoders
# MIME (Multipurpose Internet Mail Extensions)
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Use port 587 and starttls() for Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()  # Initiate TLS for secure connection

with open('password.txt', 'r') as f:
    password = f.read().strip()  # Strip to remove any trailing newline

# server.login('your_email@gmail.com', 'your_password')
server.login('mailtesting@neuralnine.com', password)

# MIMEMultipart is used for creating multipart email messages containing various parts such as plain text, HTML, and attachments
msg = MIMEMultipart()
msg['From'] = 'mailtesting@neuralnine.com'  # Use correct sender email address
msg['To'] = 'testmail@spam.de'
msg['Subject'] = 'Just a test'

# Read the message from file
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'

# Open the file using context manager
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

# Encode the payload in Base64
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
# server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', 'email_content')
server.sendmail('mailtesting@neuralnine.com', 'testmail@spam.de', text)

# Close the server connection
server.quit()