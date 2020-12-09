'''
Write tests to prove the following functionality:
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
'''

from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
import pytest 
# TDD is very importatnt in company ...ok hadeel? ok *-*


def test_insert():
    ll=LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    assert ll.head.value == 2
    assert ll.head.next.value == 1



def test_includes():
    ll=LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    assert ll.includes_node(2) == True
    assert ll.includes_node(0) == False


def test_str():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    assert ll.__str__()=='{25} -> {20} -> {15} -> {10} -> {5} -> NULL'


def test_insert_before():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.insert_before(10,-1)
    assert ll.__str__()=='{25} -> {20} -> {15} -> {-1} -> {10} -> {5} -> NULL'



def test_insert_after():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.insert_after(10,0)
    assert ll.__str__()=='{25} -> {20} -> {15} -> {10} -> {0} -> {5} -> NULL'



"""
    test case:
    Where k is greater than the length of the linked list
    Where k and the length of the list are the same
    Where k is not a positive integer
    Where the linked list is of a size 1
    “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """

def test_kth_at_end():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.kt_from_end(0)
    actual=ll.kt_from_end(0)
    assert actual==5


def test_Happy_Path():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.kt_from_end(0)
    actual=ll.kt_from_end(2)
    assert actual==15

def test_kth_at_end_invalid():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.kt_from_end(-1)
    actual=ll.kt_from_end(-1)
    assert actual=='invalid input'
    

def test_kth_at_out_side():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    ll.kt_from_end(7)
    actual=ll.kt_from_end(7)
    assert actual=='out side index'

def test_kth_empty_ll():
    ll=LinkedList()
    actual=ll.kt_from_end(7)
    assert actual=='empty linked list'





# it is not work with me :)
# @pytest.fixture
# def prep_ll():
#     ll=LinkedList()
#     ll.append(5)
#     ll.append(7)
#     return ll


# @pytest.fixture
# def prep_ll3():
#     ll=LinkedList()
#     ll.insert_node(1)
#     ll.insert_node(2)
#     return ll


# @pytest.fixture
# def prep_ll2():
#     ll=LinkedList()
#     ll.insert_node(5)
#     ll.insert_node(10)
#     ll.insert_node(15)
#     ll.insert_node(20)
#     ll.insert_node(25)
#     return ll


