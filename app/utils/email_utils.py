from flask_mail import Message
from flask import render_template
from os import environ
from app.utils.mail_extension import mail


def send_email(recipient, subject, template):
    """Sends a html email message with a subject to the specified recipient."""

    msg = Message(
        subject, recipients=[recipient], html=template, sender=environ.get("EMAIL_USER")
    )
    mail.send(msg)


def send_email_verification_message(verify_link, email):
    html = render_template("email_confirmation.html", verify_link=verify_link)
    subject = "Verify Account | STEM Diverse TV CMS"
    send_email(email, subject, html)
