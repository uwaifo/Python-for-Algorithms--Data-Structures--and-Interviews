class DequeOverstand(object):
    #Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
    def __init__(self):
        self.deque_items = []


    #    addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
    def addFront(self, item):
        #self.deque_items.insert(0,item)
        self.deque_items.append(item)

    #    addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.

    def addRear(self, item):
        self.deque_items.insert(0,item)
    
    #    removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
    def removeFront(self):
        return self.deque_items.pop()

    #    removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.  
    def removeRear(self):
        return self.deque_items.pop(0)

    #    isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.deque_items == []

    #    size() returns the number of items in the deque. It needs no parameters and returns an integer.
    def size(self):
        return len(self.deque_items)


d = DequeOverstand()
d.addFront('tits')
d.addRear('ass')
print(d.size())
print(d.removeFront() + ' ' + d.removeRear())
print(d.size())
    




        

    


    

    