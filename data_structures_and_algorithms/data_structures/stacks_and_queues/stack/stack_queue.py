class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack: #revers the linked list
    def __init__(self):
        self.top=None
    
    def push(self,data):
        node=Node(data)
        # if self.top:
        #     node.next=self.top
        #     self.top=node
        # else:
        #     self.top=node
        if self.top:#Refactre ^ 
            node.next=self.top
        self.top=node
    
    def pop(self):
        # return data
        if self.top:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value        


    def is_empty(self):
        # if count<0:
        #     return True
        # return False

        if self.top:
            return False
        return True

    def peek(self):
        return self.top.value 
    # add print function 
    def print(self):
        stg=''
        while self.top:
            # if self.top:
            #     stg+=str(self.top.value) +'->'
            stg+=str(self.top.value) +'->'
            self.top=self.top.next
        return stg


class Queue:
    def __init__(self):
        self.front=None # first value add like the first one in the queue
        self.rear=None # the last value 


    def enqueue(self, data):
        node=Node(data)
        if self.rear:
            # way one 
            # self.rear.next=node
            # sele.rear=node
            # way num 2
            old_rear=self.rear
            self.rear=node
            old_rear.next=self.rear 
        # elif not self.rear and self.front: # empty way 1
        # elif self.rear==None and self.front==None: # check emptey way 2
        else:
            # create new node and rear + front poaint to it 
            self.front=node
            self.rear=node
        
        
    def dequeue(self):
        """
        return value
        """
        if self.front:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value
        else:
            return "Queue is Empty"
        
    def peek(self):
        try:
            return self.front.value # depened in node para
            # if not self.front:
            # #Exeptions attribute error
            # raise() useless because use exceptions
        except  AttributeError:
            return 'Queue is empty'
        
        
    
    def is_empty(self):
        if self.front:
            return False
        return True




if __name__ == "__main__":
    stack=Stack()
    stack.push(5)
    stack.push(8)
    stack.push(-1)
    print(stack.peek()) 
    stack.pop()
    print(stack.peek()) #return 
    # | -1  |
    # |  8  |   
    # |__5__|

    queue=Queue()
    queue.enqueue(5)
    queue.enqueue(45)
    queue.enqueue(55)
    queue.dequeue()
    print(queue.peek())
    # 55|45|5|
    # ^     ^
    # |     |
    # rear  front