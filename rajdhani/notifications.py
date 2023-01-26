"""Email notifications on bookings.
"""
import smtplib, ssl
from email.message import EmailMessage

from . import config

def send_booking_confirmation_email(booking):
    """Sends a confirmation email on successful booking.

    The argument `booking` is a row in the database that contains the following fields:

        id, name, email, train_number, train_name, ticket_class, date
    """
    # The smtp configuration is available in the config module
    msg = EmailMessage()
    msg.set_content(
        f"""
        Hi {booking['passenger_name']},
        
        Your booking for train number '{booking['train_number']}' on {booking['date']} is confirmed.
        
        Thanks,
        Rajdhani
        """
    )
    msg["Subject"] = "Booking Confirmed"
    msg["From"] = "rajdhani@example.com"
    msg["To"] = booking['passenger_email']

    # context=ssl.create_default_context()

    with smtplib.SMTP(config.smtp_hostname, port=config.smtp_port) as smtp:
        if config.smtp_username or config.smtp_password:
            smtp.login(config.smtp_username, config.smtp_password)
        smtp.send_message(msg)