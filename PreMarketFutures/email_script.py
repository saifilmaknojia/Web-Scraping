import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(body):
    # Read credentials from file
    with open('credentials.txt') as file:
        lines = file.readlines()
        from_email  = lines[0].strip()
        from_password = lines[1].strip()
        to_email = lines[2].strip()

    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        message = MIMEMultipart()
        message['Subject'] = "Today's Pre-Market data"
        message['From'] = from_email
        message['To'] = to_email

        body_content = body
        message.attach(MIMEText(body_content, "html"))
        msg_body = message.as_string()

        # We need to allow less secure access on gmail for login to work - https://www.google.com/settings/security/lesssecureapps
        server.login(message['From'], from_password)
        server.sendmail(message['From'], message['To'], msg_body)
        server.quit()

