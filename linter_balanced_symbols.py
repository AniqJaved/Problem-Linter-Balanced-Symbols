class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return not self.items
    def __str__(self):
        return str(self.items)


symbols = {
    '{' : '}',
    '(' : ')',
    '[' : ']'
}

opener = symbols.keys()

stack = Stack()

case_1 = "({[]})"
case_2 = "(){}["

def linter(opener,symbols,stack,case):
    for symbol in case:
        #If the symbol is opening symbol
        if symbol in opener:
            stack.push(symbol)
        #If the symbol is closing symbol
        else:
            #If we had a opening symbol without any closing symbol(wether of its type or any other). For instace in case_2 we had a opening symbol without any closing tag.
            if stack.is_empty():
                return False

            #This checks that wether the closing symbol is of the same type of previous openeing symbol
            top_item = stack.pop()
            if(symbol != symbols[top_item]):
                return False
    
    if stack.is_empty():
        return True


a = linter(opener,symbols,stack,case_2)

print(a)

