from data_structures_and_algorithms.data_structures.ll_zip.ll_zip import *

def test_zip():    
    list_one = LinkedList() 
    list_two = LinkedList() 
    
    list_one.addToList(5) 
    list_one.addToList(10) 
    list_one.addToList(15) 
    
    list_two.addToList(2) 
    list_two.addToList(3) 
    list_two.addToList(20) 
    
    list_one.head = mergeLists(list_one.head, list_two.head) 
    
    actual=list_one.printList() 
    assert actual=='2 3 5 10 15 20'
