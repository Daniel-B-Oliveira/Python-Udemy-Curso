import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(sting: str):
    return bool(NUM_OR_DOT_REGEX.search(sting))

def convertToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        pass

    return valid


def isEmpty(sting: str):
    return len(sting) == 0