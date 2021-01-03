from data_structures_and_algorithms.challenges.Insertion_Sort.Insertion_Sort import InsertionSort

def test_case1():
    arr=[8,4,23,42,16,15]
    actual=InsertionSort(arr)
    assert actual==[4, 8, 15, 16, 23, 42]


def test_case2():
    arr=[20,18,12,8,5,-2]
    actual=InsertionSort(arr)
    assert actual==[-2, 5, 8, 12, 18, 20]


def test_case3():
    arr=[5,12,7,5,5,7]
    actual=InsertionSort(arr)
    assert actual==[5, 5, 5, 7, 7, 12]