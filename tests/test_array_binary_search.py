from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary

def test_case_found():
    content=[ 5,15,25,35,45,55,65,75,85] 
    x = 45
    actual=binary(content, 0, len(content)-1, x) 
    expected= 4
    assert actual==expected


def test_case_not_found():
    content=[ 5,15,25,35,45,55,65,75,85] 
    x = 10
    actual=binary(content, 0, len(content)-1, x) 
    expected= -1
    assert actual==expected
