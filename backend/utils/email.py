import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    smtp_server = None #smtp_server or "smtp.gmail.com"
    smtp_port = None #smtp_port or 587
    smtp_user = None  #smtp_user or from_email
    from_email = None #from_email or smtp_user
    smtp_password = None #smtp_password or ""

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {e}"

def send_otp_email(user_email, otp_code):
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp_code}"
    return send_email(subject, body, user_email)

