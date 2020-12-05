'''

Features
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:
# 
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
Ensure your tests are passing before you submit your solution.
'''

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0
# create a node --> add data ,next
    def append(self,data):# adding at the end o(n)
        #st1 : init current with head (i=0)
        node=Node(data)  
        if self.head==None:
            self.head=node
          # create data node 
        #st2 --> keep moving until reach ast node l
        else:
            current=self.head
            while(current.next!=None):
                current=current.next 
                #current is last node
                # make curret point to new nodes 
                current.next=node
        self.size+=1
        
    def __len__(self):
        return self.size
        

    def insert_node(self,value): #adding at beginning o(1)
        node2=Node(value,self.head)
        self.head=node2
    
    def __str__(self):
        if self.head==None:
            return('Empty linked List')
             
        # "{  } -> { b } -> { c } -> NULL"
        # {50} -> {5} -> NULL
        i=self.head
        strll=''
        while i:
            if i!=None:
                strll += str( { i.value } ) + ' -> ' 
            
                i=i.next
            if i==None:
                strll+='NULL'
        return (strll)

if __name__ == "__main__":
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    
    print(ll)
# 