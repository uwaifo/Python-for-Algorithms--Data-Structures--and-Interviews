'''
Implement a Stack

A very common interview question is to begin by just implementing a Stack! Try your best to implement your own stack!

It should have the methods:
    Check if its empty
    Push a new item
    Pop an item
    Peek at the top item
    Return the size

'''
class Stack(object):
    #stack filo
    def __init__(self):
        self.stack_items = []

    def is_empty(self):
        return self.stack_items == []

    def push(self,item):
        self.stack_items.append(item)
        return self.peek()
    
    def peek(self):
        return self.stack_items[0]
    def peek_buttom(self):
        return self.stack_items[len(self.stack_items) -1]

    def pop(self):
        self.stack_items.pop()
        
    def size(self):
        return len(self.stack_items)


    
        
my_stack = Stack()
print('Empty ?',my_stack.is_empty())
print(my_stack.push('Uwaifo'))
print(my_stack.push('Victor'))
print(my_stack.push('Idehenre'))

print('top item is ',my_stack.peek())
print('last item is ',my_stack.peek_buttom())
print(my_stack.size())
print(my_stack.push('Ngozi'))
print(my_stack.size())
my_stack.pop()
my_stack.pop()
print(my_stack.size())
print(my_stack.peek())
print(my_stack.peek_buttom())








