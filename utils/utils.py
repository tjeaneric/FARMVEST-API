import random
import string


def generate_code(digits=6):
    key = "".join(random.choices(string.ascii_uppercase + string.digits, k=digits))
    return key
