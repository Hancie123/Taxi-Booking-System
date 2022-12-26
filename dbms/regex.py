import re

def checkemail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        emailResult=True

    else:
        emailResult=False

    return emailResult

def checkphone(mobile):
    regex=re.compile("^(?:0|\+?977)\s?(?:\d\s?){9,11}$")
    if re.fullmatch(regex, mobile):
        mobileResult=True
    else:
        mobileResult=False

    return mobileResult

def checkcredit(credit):
    regex=re.compile("(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}")
    if re.fullmatch(regex, credit):
        creditResult=True
    else:
        creditResult=False
    return creditResult


def namevalidation(name):
    regex=re.compile("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    if re.fullmatch(regex, name):
        nameResult=True
    else:
        nameResult=False
    return nameResult


def passwordvalidation(password):
    regex=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if re.fullmatch(regex, password):
        passwordResult=True
    else:
        passwordResult=False
    return passwordResult
