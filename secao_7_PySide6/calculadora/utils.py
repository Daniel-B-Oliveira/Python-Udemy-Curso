import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(sting: str):
    return bool(NUM_OR_DOT_REGEX.search(sting))

def isEmpty(sting: str):
    return len(sting) == 0