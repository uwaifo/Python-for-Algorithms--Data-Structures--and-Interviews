'''
Before we implement our own Stack class, let's review the properties and methods of a Stack.
The stack abstract data type is defined by the following structure and operations. 
A stack is structured, as described above, as an ordered collection of items where items are added to and removed from the end called the “top.” 
Stacks are ordered LIFO. The stack operations are given below.
'''

class StackOverstand(object):
    #init to construct
    #Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.    
    def __init__(self):
        self.items = []
       

    #    push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
    def push(self,item):
        self.items.append(item)
        

    #pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    def pop(self):
        return self.items.pop()# this is standard list pop functionality
    
    #    peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    def peek_buttom(self):
        #return self.items[0]# incorrect
        return self.items[len(self.items) - 1]
        return self.items[len(self.items) - 1]


    def peek_top(self):
       return self.items[0]
        
    #isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    #size() returns the number of items on the stack. It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)
        

my_stack = StackOverstand()
print(my_stack.isEmpty())
my_stack.push('me')
my_stack.push('you')
my_stack.push('them')

print(my_stack.peek_buttom())
print(my_stack.peek_top())
print(my_stack.pop())
print(my_stack.size())
'''
my_stack.push(True)
print(my_stack.isEmpty())
print(my_stack.size())
my_stack.push("one ass hole")
my_stack.push('more ass holes')
my_stack.pop()
print(my_stack.size())
print(my_stack.peek_top())

'''

