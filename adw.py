
import smtplib  # For sending emails
from email.mime.text import MIMEText  # For plain text in the email
from email.mime.multipart import MIMEMultipart  # For creating a multipart message
from email.mime.base import MIMEBase  # For handling attachments
from email import encoders  # For encoding attachments
import os  # For file path operations

# SMTP configuration
smtp_server = "smtp.gmail.com"  # Corrected the SMTP server address
smtp_port = 465  # Correct SMTP port for TLS

# Sender and receiver details
sender_mail = "anupamdesharaju764@gmail.com"
email_password = "anupam12345@"  # Note: Avoid hardcoding sensitive information
receiver_mail = "21ag1a0583@gmail.com"

# Email content
subject = "This mail includes an attachment"
body = "Hi, this is a test mail from Python."

# Compose email
message = MIMEMultipart()
message["From"] = sender_mail
message["To"] = receiver_mail
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Sending email
try:
    # Establish connection to the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption

    # Login to the sender's email account
    server.login(sender_mail, email_password)

    # Send the email
    server.sendmail(sender_mail, receiver_mail, message.as_string())
    print("Mail sent successfully!")
except Exception as e:
    print(f"Unable to send mail: {e}")
finally:
    # Always close the server connection
    server.quit()
