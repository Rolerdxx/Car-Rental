from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os



def SendEmail(towho, subject, message):
    print(towho)
    print(subject)
    print(message)
    message = Mail(
        from_email='carrentalapp123@gmail.com',
        to_emails=towho,
        subject=subject,
        html_content=message)
    print(os.environ.get('SENDGRID_API_KEY'))
    sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
