from data_structures_and_algorithms.challenges.Merge_Sort.merge_sort import MergeSort

def test_case1():
    arr = [12, 11, 13, 5, 6, 7]
    actual=MergeSort(arr)
    expected=[5, 6, 7, 11, 12, 13]
    assert actual==expected

def test_case():
    arr = [20,18,12,8,5,-2]
    actual=MergeSort(arr)
    expected=[-2, 5, 8, 12, 18, 20]
    assert actual==expected


def test_case3():
    arr = [2,3,5,7,13,11]
    actual=MergeSort(arr)
    expected=[2, 3, 5, 7, 11, 13]
    assert actual==expected
