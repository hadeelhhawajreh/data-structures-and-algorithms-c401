class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def add(self,key,value):
        new=Node(key,value)
        if not self.head:
            self.head=new
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new

class HashTable:
    def __init__(self,size=1024):
        self.size=size
        self.map=[None]*size

    def hash(self,key):
        """
        1. take a
        Args:
            takes key 
        Returns:
            return index 
        """        
        sum=0
        for i in key:
            sum+=ord(i)
        sum*=17
        sum %= self.size  
        return sum
    
    def set(self,key,value):
        """
        takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed
        """
        hash_key = self.hash(key)
        if self.map[hash_key] == None:
            self.map[hash_key] = Linkedlist()
            self.map[hash_key].add(key,value)
        else:
            current = self.map[hash_key].head
            while current:
                if current.value == key:
                    current.value =None
                    current.value = (key,value)
                elif current.next == None:
                    self.map[hash_key].add(key,value)
                current = current.next
 


    # def set(self,key,value):
    #     hash_key=self.hash(key)
    #     # print(hash_key)
        
    #     if self.map[hash_key] == None:      
    #         self.map[hash_key]=Linkedlist()
    #         self.map[hash_key].add(key,value)
    #     else:        
    #         self.map[hash_key].add(key,value)
    
    def get(self,key):
        indx=self.hash(key)
        current=self.map[indx].head
        while current:
            if  current.key==key:
                return current.value
            current=current.next
    def containes(self,key):
        indx=self.hash(key)
        current=self.map[indx].head
        while current:
            if  current.key==key:
                return True
            current=current.next
            return False





if __name__ == "__main__":
    h=HashTable(1024)
    h.set('cloud',5)
    
    print(h.get('cloud'))
    print(h.containes('cloud'))
    # h.set('colud',10)
    # h.set('clodu',15)
    # key='cloud'
    # sum=0
    # for i in key:
    #     sum+=ord(i)
    # sum*=17
    
    # sum %= self.size  
    # print(sum) 