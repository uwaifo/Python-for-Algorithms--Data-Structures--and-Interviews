'''
Queue Methods and Attributes
Before we begin implementing our own queue, let's review the attribute and methods it will have:

'''

class QueueOverstand(object):
    #Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
    def __init__(self):
        self.queue_items = []
        
    #enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
    def enqueue(self, param):
        #FIFO
        #here we use the standard list.insert method to put params at the indicated position  of the queuse
        # here we put it in the 0 index position ie first
        self.queue_items.insert(0,param)
        return self.peep_top()

    #dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    def dequeue(self):
        #FIFO
        #here again we use the standard list pop method to remove from the buttom of the qeueu
        #Note that the items at the buttom are the first to have come in
        return self.queue_items.pop()

    #isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.queue_items == []
        '''
        if len(self.queue_items) == 0:
            return True
        else:
            return False
        '''

    #size() returns the number of items in the queue. It needs no parameters and returns an integer.
    def size(self):
        return len(self.queue_items)

    def peep_top(self):
        return self.queue_items[0]


food_line = QueueOverstand()
print(food_line.isEmpty())
print(food_line.enqueue('Uwaifo'))
print(food_line.size())
print(food_line.enqueue('Ifeanyi'))
print(food_line.size())
print(food_line.dequeue())
print(food_line.size())
print(food_line.isEmpty())






    
        
    

        