from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_otp_email(user_email, otp):
   
    subject = "🔒 Verify Your  Account"


    html_content = render_to_string(
        "emails/verify_email.html", {"email": user_email, "otp": otp}  
    )

    email = EmailMessage(
        subject=subject,
        body=html_content,
        to=[user_email],
    )
    email.content_subtype = "html"  
    email.send()
