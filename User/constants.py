def farmtype():

    type_of_farm = {"CROPS": "CROPS", "LIVESTOCK": "LIVESTOCK"}

    multi_choice = []

    for choice in type_of_farm:
        multi_choice.append((choice, type_of_farm[choice]))

    return tuple(multi_choice)


def Gender():
    """
    Choices of Gender.
    """
    Gender = {"MALE": "MALE", "FEMALE": "FEMALE", "RATHER NOT SAY": "RATHER NOT SAY"}
    multi_choice = []

    for choice in Gender:
        multi_choice.append((choice, Gender[choice]))

    return tuple(multi_choice)


def Role():
    """
    Choices of Role.
    """
    Role = {"FARMER": "FARMER", "INVESTOR": "INVESTOR"}

    multi_choice = []

    for choice in Role:
        multi_choice.append((choice, Role[choice]))

    return tuple(multi_choice)


def States():

    states = {
        "ABIA": "ABIA",
        "ABUJA": "ABUJA",
        "ADAMAWA": "ADAMAWA",
        "AKWA IBOM": "AKWA IBOM",
        "ANAMBRA": "ANAMBRA",
        "BAUCHI": "BAUCHI",
        "BAYELSA": "BAYELSA",
        "BENUE": "BENUE",
        "BORNO": "BORNO",
        "CROSS RIVER": "CROSS RIVER",
        "DELTA": "DELTA",
        "EBONYI": "EBONYI",
        "EDO": "EDO",
        "EKITI": "EKITI",
        "ENUGU": "ENUGU",
        "GOMBE": "GOMBE",
        "IMO": "IMO",
        "JIGAWA": "JIGAWA",
        "KADUNA": "KADUNA",
        "KANO": "KANO",
        "KATSINA": "KATSINA",
        "KEBBI": "KEBBI",
        "KOGI": "KOGI",
        "KWARA": "KWARA",
        "LAGOS": "LAGOS",
        "NASAWARA": "NASAWARA",
        "NIGER": "NIGER",
        "OGUN": "OGUN",
        "ONDO": "ONDO",
        "OSUN": "OSUN",
        "OYO": "OYO",
        "PLATEAU": "PLATEAU",
        "RIVERS": "RIVERS",
        "SOKOTO": "SOKOTO",
        "TARABA": "TARABA",
        "YOBE": "YOBE",
        "ZAMFARA": "ZAMFARA",
    }
    multi_choice = []

    for choice in states:
        multi_choice.append((choice, states[choice]))

    return tuple(multi_choice)
