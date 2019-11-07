'''
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.
You can assume the input string has no spaces.
'''
class Stack(object):
    def __init__(self): 
        self.stack_items = []
    
    def isEmpty(self):
        return self.stack_items == []

    def push(self, item):
        self.stack_items.insert(0,item)

    def peek_top(self):
        return self.stack_items[0]

    def peek_buttom(self):
        return self.stack_items[len(self.stack_items) - 1]
    

    def pop(self):
        self.stack_items.pop()

    def size(self):
        return len(self.stack_items)


def balance_check(s):
    
    if len(s) % 2 != 0:
        return False
    stack = []
    opening_paren = set('({[')
    closing_paren = set(']})')
    matching_pairs = zip(opening_paren,closing_paren)
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    for paren in s:
        if paren in opening_paren:
            stack.append(paren) 
        else:
            if len(stack) ==0:
                return False
            
            last_open = stack.pop()
    
            if(last_open,paren) not in matches:
                return False
        
    return len(stack) == 0
    

    
         
print(balance_check('[]')) 
#print(balance_check('[](){([[[]]])}'))
#print(balance_check('[](){([[[]]])}'))




'''
caller = Stack()
caller.push('[')
caller.push(']')

print(caller.isEmpty())
print(caller.peek_top())
print(caller.peek_buttom())
print(caller.size())
caller.pop()
print(caller.size())


        
 
#txt = "}"[::-1]
#print(txt)
'''