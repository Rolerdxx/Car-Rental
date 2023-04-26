from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def SendEmail(towho, subject, message):
    message = Mail(
        from_email='carrentalapp123@gmail.com',
        to_emails=towho,
        subject=subject,
        html_content=message)
    sg = SendGridAPIClient('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')
    sg.send(message)
