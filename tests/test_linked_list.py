from data_structures_and_algorithms.challenges.linked_list.linked_list import *
import pytest 
def test_append(prep_ll):
    # ll=LinkedList()
    # ll.append(5)
    # ll.append(7)
    assert prep_ll.head.value == 5
    assert prep_ll.head.next.value == 7
    assert prep_ll.head.next.next == None

def test_length(prep_ll):
    # ll=LinkedList()
    # ll.append(5)
    # ll.append(7)
    assert len(prep_ll)==2
# TDD is very importatnt in company ...


def test_insert(prep_ll3):
    assert prep_ll.head.value == 2
    assert prep_ll.head.next.value == 1


def test_str(prep_ll2):
    assert prep_ll.__str__()=="{25} -> {20} -> {15} -> {10} -> {5} -> NULL"

@pytest.fixture
def prep_ll():
    ll=LinkedList()
    ll.append(5)
    ll.append(7)
    return ll


@pytest.fixture
def prep_ll3():
    ll=LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    return ll


@pytest.fixture
def prep_ll2():
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    return ll

