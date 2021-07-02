def Payment_Method():
    """
    Choice of payment
    """
    Payment_Method= {"CREDIT CARD": "CREDIT CARD", "PAYPAL": "PAYPAL", "BANK TRANSFER": "BANK TRANSFER"}
    multi_choice = []

    for choice in Payment_Method:
        multi_choice.append((choice, Payment_Method[choice]))

    return tuple(multi_choice)
