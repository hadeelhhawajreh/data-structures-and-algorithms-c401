from data_structures_and_algorithms.challenges.Quick_sort.quick_sort import *

def test_case1():
    arr = [12, 11, 13, 5, 6, 7]
    actual=quick_sort(arr,0,len(arr)-1)
    expected=[5, 6, 7, 11, 12, 13]
    assert actual==expected

def test_case():
    arr = [10, 80, 30, 90, 40, 50, 70]
    actual=quick_sort(arr,0,len(arr)-1)
    expected=[10,30,40,50,70,80,90]
    assert actual==expected


def test_case3():
    arr = [2,3,5,7,13,11]
    actual=quick_sort(arr,0,len(arr)-1)
    expected=[2, 3, 5, 7, 11, 13]
    assert actual==expected
