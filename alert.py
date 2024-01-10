import smtplib

def send_alert():
    subject = 'Alert: Unauthorized access detected'
    body = 'Someone has accessed the server.'
    message = f'Subject: {subject}\n\n{body}'

    sender_email = "arunbalaji17ab@gmail.com"
    recipient_email = "arunbalaji.ml@gmail.com"
    password = "rxrlqohacflkmoje"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, recipient_email, message)
            print('Email sent successfully.')
    except smtplib.SMTPException as e:
        print('Error sending email:', e)
        if isinstance(e, smtplib.SMTPAuthenticationError):
            print(sender_email)
            print(password)
            print('Invalid credentials. Please check your username and password.')
        else:
            print('An error occurred while sending the email.')

def send_alert2():
    subject = 'Alert: System down'
    body = 'System is down due to some erroe..'
    message = f'Subject: {subject}\n\n{body}'

    sender_email = "arunbalaji17ab@gmail.com"
    recipient_email = "arunbalaji.ml@gmail.com"
    password = "rxrlqohacflkmoje"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, recipient_email, message)
            print('Email sent successfully.')
    except smtplib.SMTPException as e:
        print('Error sending email:', e)
        if isinstance(e, smtplib.SMTPAuthenticationError):
            print(sender_email)
            print(password)
            print('Invalid credentials. Please check your username and password.')
        else:
            print('An error occurred while sending the email.')
