import pytest

import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from proj.converter import generate_cusip8, generate_cusip_checkdigit, convert

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

def test_generate_checkdigit(input,output):
    test = 0
    assert("test" == test)

def test_convert(input):
    test = 0
    assert("test" == test)
