class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
      
    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      
    @classmethod
    def from_array(cls, arr):
        if arr==[]:return None
        return Cons(arr[0],Cons.from_array(arr[1:])) if arr!=[] else None
        
    
    def filter(self, fn):
        if fn(self.head)==True:
            return Cons(self.head,self.tail.filter(fn)) if self.tail!=None else Cons(self.head,None)
        else:
            return self.tail.filter(fn) if self.tail!=None else None

    
    def map(self, fn):
        return Cons(fn(self.head),self.tail.map(fn)) if self.tail!=None else Cons(fn(self.head),None)

numbers = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, None)))))
print(Cons.from_array([1,2,3,4,5]).to_array())