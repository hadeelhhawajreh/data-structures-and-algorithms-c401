from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import *


def test_multibracketvalidation_true():
    x=multibracketvalidation('{[]{()}}')
    actual=x
    assert actual==True

def test_multibracketvalidation_false():

    x=multibracketvalidation('{[]{(])}}')
    actual=x
    assert actual==False


def test_multibracketvalidation_three():

    x=multibracketvalidation('()[[Extra Characters]]')
    actual=x
    assert actual==True

    # {}{Code}[Fellows](())	

def test_multibracketvalidation_four():

    x=multibracketvalidation('(){}[[]]')
    actual=x
    assert actual==True

def test_multibracketvalidation_five():

    x=multibracketvalidation('{}{Code}[Fellows](())')
    actual=x
    assert actual==True
