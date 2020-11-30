from data_structures_and_algorithms.challenges.array_shift.array_shift import add_middle

def test_shifting():
    a=[1,2,3,4,5,6,7]
    actual=add_middle(a,10)
    expected=[1, 2, 3, 10, 4, 5, 6, 7]
    assert actual==expected
