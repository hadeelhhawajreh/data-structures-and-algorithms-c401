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

    def kt_from_end(self,k):
        if k>=0:
            if self.head==None:
                return 'empty linked list'
            else:
                i=0
                current=self.head
                while current:
                    current=current.next
                    i+=1
                if  i-1<k:
                    return 'out side index'
               

                else:
                    index=i-k
                    current=self.head
                    for j in range(index-1):
                        current=current.next
                    return current.value
        else:
            return 'invalid input'
         
        

    def insert_node(self,value): #adding at beginning o(1)
        '''
        This method  takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
        '''
        node2=Node(value,self.head)
        self.head=node2
    
    def __str__(self):
        '''
         this method takes  return a string representing all the values in the Linked List, formatted as:
          "{ a } -> { b } -> { c } -> NULL"
        '''

        if self.head==None:
            return('Empty linked List')
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
                current=current.next
        return False

    def insert_before(self,indx,val):
        node3=Node(val)
        if not self.includes_node(indx):
            return 'value not found '
        elif self.head.value==indx:
            self.insert_node(val)
        else:
            i=self.head
            while i.next!=None:
                if i.next.value==indx:
                    node3.next=i.next
                    i.next=node3
                    break
                i=i.next
        
    def insert_after(self,indx,val):
        print('index',indx)
        node3=Node(val)
        if not self.includes_node(indx):
            return 'value not found '
        else:
            i=self.head
            while i.next!=None:
                if i.value==indx:
                    node3.next=i.next
                    i.next=node3
                    break
                i=i.next
            i.next=node3

    def append(self,data):
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
    
    # def isPalind(self):
    #     cur=self.head
    #     op=[]
    #     while cur:
    #         op.append(cur.value)
    #         cur=cur.next
        
    #     # print(len(op))
    #     n=len(op)
    #     print(op)
    #     print(op[-2])

    #     for i in range(len(op)):
    #         print('iiiiii',i,op[i],-i-1,op[-i-1])
    #         if op[i]==op[i-i] and i != n and i-1 !=n and len(op)!=1:
    #             # if op[i] and op[len(op)-1] ==n:
    #             v=op.pop(i)
    #             v2=op.pop()
    #             print('oooooooooooopppppppp',op)
                
    #             print('v,v2',v,v2)
        
    #     if len(op)==1:
    #         return True
    #     return False
    def palind(self):
        list2 = []
        current =self.head
        while current:
            list2.append(current.value)
            current= current.next
        print('list',list2)
        print(' reversed list ',list2[::-1])

        for ele in list2[::-1]:
            current=self.head
            if ele==current.value:
                return True
            return False
    

    def reversed(self):
        list=[]
        reverse=[]
        cur=self.head
        while cur:
            list.append(cur.value)
            cur=cur.next
        # print(list)
        for i in range(len(list)):
            reverse.append(list[-i-1])
            # reverse.append(list.pop())
        return reverse

        

        # pal=True
        # while current:
        #     value=list2.pop()
        #     print(pal)
        #     if current.value==value:
        #         pal=True
        #     else:
        #         pal= False
        #     current=current.next
        # return pal

        # isPalind =True
        # while current:
        #     value= list2.pop()
        #     if current.value == value :
        #         isPalind = True
        #     else:
        #         isPalind=False
        #     current = current.next
        # return isPalind

if __name__ == "__main__":
    ll=LinkedList()
    ll.insert_node(5)
    ll.insert_node(10)
    ll.insert_node(15)
    ll.insert_node(20)
    ll.insert_node(25)
    # {25} -> {20} -> {15} -> {10} -> {5} -> NULL
    print(ll.insert_after(10,0))
    print(ll.insert_before(5,-1))
    print(ll.insert_after(5,-20))
    l2=LinkedList()
    l2.insert_node(5)
    l2.insert_node(10)
    l2.insert_node(15)
    l2.insert_node(10)
    l2.insert_node(5)
    print(ll.palind())
    print(l2.palind())
    print(ll)
    print(ll.reversed())
    # print(ll.kt_from_end(2))