class Queue(object):
    def __init__(self):
        self.queue_items = []

    def is_empty(self):
        return self. queue_items == []
    def enqueue(self, item):
        self.queue_items.insert(0,item)

    def dequeue(self):
        self.queue_items.pop()
    def size(self):
        return len(self.queue_items)

    def peeper(self,l_r):

        #if l_r is not 'l' or l_r is not 'r':
        #   return
        if l_r == 'r':
            return self.queue_items[len(self.queue_items)-1]
        if l_r == 'l':
            return self.queue_items[0]

cutie = Queue()
cutie.enqueue('Maria')
print(cutie.is_empty())
cutie.enqueue('Mary')
print(cutie.size())
cutie.enqueue('Patience')
print(cutie.size())
print(cutie.peeper('r'))
print(cutie.peeper('l'))

cutie.dequeue()
print(cutie.peeper('r'))




