class Node:
    '''
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    '''
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
          # --> keep moving until reach ast node l
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
        '''
        This method  takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
        '''
        node2=Node(value,self.head)
        self.head=node2
        self.size+=1
    
    def __str__(self):
        '''
         this method takes  return a string representing all the values in the Linked List, formatted as:
          "{ a } -> { b } -> { c } -> NULL"
        '''

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

    def includes_node(self,inc_val):
        '''
        this  method takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        '''
        current=self.head
        while current!= None:
            if current.value==inc_val:
                return True
            else:
                current.next
            return False

if __name__ == "__main__":
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10) 

    print(ll.includes_node(10))
