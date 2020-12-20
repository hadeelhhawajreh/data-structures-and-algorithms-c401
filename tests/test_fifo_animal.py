from  data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import *

def test_enqueu():
    animal = AnimalShelter()
    animal.enqueue(Dog('cat_name'))
    animal.enqueue(Cat('dog_name'))

    animal.enqueue(Cat('bsboos'))
    animal.enqueue(Dog('bobi'))
    assert animal.front.name == 'cat_name'
    assert animal.front.next.name == 'dog_name'
    assert animal.front.next.next.name=='bsboos'
    assert animal.front.next.next.next.name=='bobi'

def test_dequeue_dog():
    animal = AnimalShelter()
    animal.enqueue(Cat('cat_name'))
    animal.enqueue(Dog('dog_name'))
    animal.enqueue(Dog('dog_name2'))
    assert animal.dequeue('dog')== 'dog_name'



def test_dequeue_cat():
    animal = AnimalShelter()
    animal.enqueue(Cat('cat_name'))
    animal.enqueue(Dog('dog_name'))
    assert animal.dequeue('cat')== 'cat_name'


