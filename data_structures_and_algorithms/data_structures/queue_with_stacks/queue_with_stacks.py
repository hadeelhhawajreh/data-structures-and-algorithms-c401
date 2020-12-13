class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class PseudoQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]


    def stackDequeue(self): #1 2 3
        # push from here 
        try:

            if  len(self.stack1) <0:
                return 'Empty Queue '
            else:   
                x=self.stack1[-1]
                self.stack1.pop()
                return x
        except IndexError:
            return f' an error occured',IndexError

    def stackEnqueue(self,val):
        try:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
            
            self.stack1.append(val)

            while len(self.stack2)!=0:
                self.stack1.append(self.stack2[-1])
                self.stack2.pop()
        except Exception:
            return f' an error occured {Exception}'




class Stack: 
    def __init__(self):
        self.top=None
    
    def push(self,data):
        node=Node(data)
        if self.top:
            node.next=self.top
        self.top=node
    
    def pop(self):
        if self.top:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value        

    
            

    def is_empty(self):
        if self.top:
            return False
        return True

    def peek(self):
        return self.top.value 

if __name__ == "__main__":
    q=PseudoQueue()
    q.stackEnqueue(20)
    # q.stackEnqueue(15)
    # q.stackEnqueue(10)
    print(q.stackDequeue())
    print(q.stackDequeue())
    print(q.stackDequeue())

    # print(q.print())

#  enqueue --> 
#  three->two->one
# stack.push(stack.pop()) return 
#
# enqueue
# top
# |
# 
# Three
# Two
# One

# dequeue 
# push(pop())

# one deque --> 1
# two -->2 
# three -->3