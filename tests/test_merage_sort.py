from data_structures_and_algorithms.challenges.Merge_Sort.merge_sort import Mergesort

def test_case1():
    arr = [12, 11, 13, 5, 6, 7]
    actual=Mergesort(arr)
    expected=[5, 6, 7, 11, 12, 13]
    assert actual==expected

def test_case():
    arr = [20,18,12,8,5,-2]
    actual=Mergesort(arr)
    expected=[5, 6, 7, 11, 12, 13]
    assert actual==expected


