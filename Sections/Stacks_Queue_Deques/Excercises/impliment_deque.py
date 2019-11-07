class Deque(object):
    def __init__(self, *args): 
        self.deque_items = []

    def isEmpty(self):
        return self.deque_items == []

    def add(self, direction, item):
        if direction != 'f' and direction != 'b':
            return None

        if direction == 'f':
            self.deque_items.insert(0,item)

        if direction == 'b':
            self.deque_items.append(item)

    def remove(self, direction, item):
        
        if direction != 'f' and direction != 'b':
            return None
        if direction == 'f':
            self.deque_items.pop()

        if direction == 'b':
            self.deque_items.pop()

    def  size(self):
        return len(self.deque_items)


object_one = Deque()
object_one.add('f','James')
object_one.add('b','Jimmy')

print(object_one.size())




