'''
Given the Stack class below, implement a Queue class using two stacks! Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
The key insight is that a stack reverses order (while a queue doesn't). A sequence of elements pushed on a stack comes back in reversed order when popped. Consequently, two stacks chained together will return elements in the same order, since reversed order reversed again is original order.

We use an in-stack that we fill when an element is enqueued and the dequeue operation takes elements from an out-stack. If the out-stack is empty we pop all elements from the in-stack and push them onto the out-stack. 
'''

class Queue2Stacks(object):
    def __init__(self):  
        # Two Stacks
        self.in_stack = []
        self.out_stack = []
    #though title a stack class this method impliments a queeu
    #so we append from the front to banck or enque
    def enqueue(self,element):
        #self.in_stack.insert(0,element)
        self.in_stack.append(element)

    def dequeue(self): 
        # if out stack is empty
        if not self.out_stack:
        #while there is somthing in in_stack
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

                
     
    
two_stack = Queue2Stacks()
 
two_stack.enqueue('one')
two_stack.enqueue('two')
print(two_stack.out_stack[0])
print(two_stack.in_stack[0])
#print(two_stack.stack2[1])