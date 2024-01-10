import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def execute_command_and_send_email():
    # Execute command
    command = "ipconfig"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Save the output to a text file
    file_path = r"D:\output.txt"
    with open(file_path, "w") as file:
        file.write(result.stdout)

    print(f"Output saved to 'output.txt'")

    # Send email with attachment
    send_email(
        to_email="arunbalaji.ml@gmail.com",
        subject="Command Output Attachment",
        body="Please find the attached command output.",
        attachment_path=file_path
    )

def send_email(to_email, subject, body, attachment_path):
    # Set up the email
    sender_email = "arunbalaji17ab@gmail.com"
    sender_password = "rxrlqohacflkmoje"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach body text
    message.attach(MIMEText(body, "plain"))

    # Attach file
    attachment = open(attachment_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
    message.attach(part)

    # Connect to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

# Example usage
execute_command_and_send_email()
