from django.core.mail import send_mail


def send_email(email, message, subject):
    """
    :param str email: Email address to receive the code
    :param str message: Message to be sent to the recipients
    :param str subject: Email subject
    """
    print(f"{message} has been sent to {email}")

    send_mail(subject, message, "ericjohn415@gmail.com", [email], fail_silently=False)
