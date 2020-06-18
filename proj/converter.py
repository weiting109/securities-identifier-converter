from datetime import datetime

def split_bbticker(bbticker):
    """
    Given a Bloomberg ticker as a string, return:
    - string ticker prefix
    - string expiry month (mapped character)
    - string expiry year
    - string sector
    """

    running = "" # ticker and month
    for c in bbticker:
        if ord(c) < ord("0") or ord(c) > ord("9"):
            running+=c
        else: break
    prefix_ticker = running[:-1].rstrip()
    month = running[-1]

    bbticker = bbticker[len(running):] # remainder of string
    running = bbticker.split() # expiry year and sector separated by space
    year, sector = running[0], running[1]

    # resolving truncated years to expiry years
    currYear = datetime.now().year
    if len(year)==1:
        year = ''.join([str(currYear//10),year])
    else:
        year = ''.join([str(currYear//100),year])

    return prefix_ticker,month,year,sector

def generate_cusip(bbticker):
    """
    Given a bloomberg ticker as a string, return a string of 8 alphanumeric
    characters (modified CUSIP without checkdigit).
    """

    return void

def generate_checkdigit():
    return void

def convert():
    return void

bbtickers = ['AIH8 Index','C Z7 Comdty','LAZ18 Comdty','OATZ7 Comdty']
for t in bbtickers:
    print(split_bbticker(t))
