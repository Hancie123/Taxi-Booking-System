import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def emailvalidation(email):
    if re.fullmatch(regex, email):
        result=True

    else:
        result=False

    return result

