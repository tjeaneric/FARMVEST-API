def send_sms(phone_numbers, message):
    """
    :param list[str] phone_numbers: list of phone numbers to receive sms message. Country code must be included
    :param str message: SMS message to be sent to the recipients
    """
    print(f"{message} has been sent to {phone_numbers}")
