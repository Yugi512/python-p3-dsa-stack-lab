class Stack:

    def __init__(self, items = [],limit= None ):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.size() == self.limit:
            return self.items
        else:
            self.items.append(item)
            

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()
             

    def peek(self):
        return(self.items[-1])
    
    def size(self):
        return len(self.items)

    def full(self):
        fulls = self.size() - self.limit
        if fulls == 0:
            return True
        else:
            return self

    def search(self, target):
        
        if target in self.items:
            index = 1
            if self.items.index(target) == 0:
                return self.size() - index
                index += 1 
            else:
                index += self.items.index(target)
                print(self.size() - index)
                return self.size() - index
        else:
            return -1   