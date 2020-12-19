class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next
class Cat():
    def __init__(self,name):
        self.name = name
        self.type = 'cat'
    
   
class Dog():
    def __init__(self,name):
        self.name = name
        self.type = 'dog'


class AnimalShelter():
   
    def __init__(self):
        self.front= None
        self.rear = None

    def enqueue(self,data):
        node= data
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self,pref=None):
        try:
            if self.front.type == pref:
                temp = self.front
                self.front = self.front.next
                return temp.name
                    
            else:
                temp = self.front
                while temp:
                    if temp.next.type == pref:
                        current = temp.next.name
                        temp.next = temp.next.next
                        return current
                    else:
                        temp = temp.next
               
          
        except AttributeError :
            return ' null '








if __name__ == "__main__":
    c=Cat('cat one')
    c2=Cat('cat two')
    d=Dog('dog 1')
    d2=Dog('dog 2')
    animal=AnimalShelter()   
    animal.enqueue(c)
    animal.enqueue(d)  
    animal.enqueue(c2)
    animal.enqueue(d2) 
    print(animal.dequeue('cat'))

