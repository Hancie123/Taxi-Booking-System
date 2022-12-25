import re

# Function to validate Gender
def timevalidation(time):

    # Regex to check valid time
    regex=re.compile("(0[1-9]|1[0-2]):([0-5][0-9]) ((a|p)m|(A|P)M)")
    if re.fullmatch(regex, time):
        timeResult=True
    else:
        timeResult=False

    return timeResult

