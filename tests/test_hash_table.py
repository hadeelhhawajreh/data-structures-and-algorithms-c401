from data_structures_and_algorithms.challenges.HashTable.hashtable import *

def test_set_and_get():
    h=HashTable(1024)
    h.set('cloud',5)
    
    assert h.get('cloud')==5
    print(h.containes('cloud'))

def test_containes():
    h=HashTable(1024)
    h.set('cloud',5)
    
    assert h.containes('cloud')==True