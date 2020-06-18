import pytest

import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from proj.converter import generate_cusip8, generate_cusip_checkdigit, convertBbtoCUSIP

@pytest.fixture
def input():
    bbtickers = ['AIH8 Index','C Z7 Comdty','LAZ18 Comdty','OATZ7 Comdty']
    return bbtickers

@pytest.fixture
def output():
    mod_cusip = ['AIH820284','CZ7202773','LAZ820180','OATZ72029']
    return mod_cusip

def test_generate_cusip8(input,output):
    """
    Test generate_cusip8 function, which returns a string of 8 alphanumeric
    characters (modified CUSIP without checkdigit)
    """
    for i in range(len(input)):
        assert(output[i][:8] == generate_cusip8(input[i]))

def test_generate_cusip_checkdigit(input,output):
    """
    Test generate_cusip_checkdigit function, which returns a int check digit
    when given a string of 8-alphanumeric-character CUSIP.
    """
    for i in range(len(input)):
        assert(generate_cusip_checkdigit(output[i][:8]) == int(output[i][-1]))

def test_convertBbtoCUSIP(input, output):
    """
    Test convertBbtoCUSIP function, which return 9-alphanumeric-character
    modified CUSIP given Bloomberg ticker as a string.
    """
    for i in range(len(input)):
        assert(convertBbtoCUSIP(input[i]) == output[i])
