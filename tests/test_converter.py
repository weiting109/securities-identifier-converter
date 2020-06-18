import pytest

import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from proj.converter import generate_checkdigit

@pytest.fixture
def input():
    bbtickers = ['AIH8 Index','C Z7 Comdty','LAZ18 Comdty','OATZ7 Comdty']
    return bbtickers

def test_generate_checkdigit(input):
    test = 0
    assert("test" == test)

def test_convert(input):
    test = 0
    assert("test" == test)
