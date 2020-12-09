""" Python program to merge two 
sorted linked lists """
  
  
# Linked List Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
# Create & Handle List operations 
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # Method to display the list 
    def printList(self): 
        temp = self.head 
        while temp: 
            print(str(temp.data), end=' ') 
            temp = temp.next
        return
    # Method to add element to list 
    def addToList(self, newData): 
        newNode = Node(newData) 
        if self.head is None: 
            self.head = newNode 
            return
  
        last = self.head 
        while last.next: 
            last = last.next
  
        last.next = newNode 
  
  
# Function to merge the lists 
# Takes two lists which are sorted 
# joins them to get a single sorted list 
def mergeLists(first, seconed): 
  
    # A dummy node to store the result 
    temp = Node(0) 
  
    # end stores the last node 
    end = temp 
    while True: 
  
        # If any of the list gets completely empty 
        # directly join all the elements of the other list 
        if first is None: 
            end.next = seconed 
            break
        if seconed is None: 
            end.next = first 
            break
  
        # Compare the data of the lists and whichever is smaller is 
        # appended to the last of the merged list and the head is changed 
        if first.data <= seconed.data: 
            end.next =first 
            first =first.next
        else: 
            end.next = seconed 
            seconed = seconed.next
  
        # Advance the end 
        end = end.next
  
    # Returns the head of the merged list 
    return temp.next
  
  
list_one = LinkedList() 
list_two = LinkedList() 
  
list_one.addToList(5) 
list_one.addToList(10) 
list_one.addToList(15) 
  
list_two.addToList(2) 
list_two.addToList(3) 
list_two.addToList(20) 
  
list_one.head = mergeLists(list_one.head, list_two.head) 
  
list_one.printList() 
  
