class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


def bracket_parse(s1):
    matched = {")":"(", "]":"[", "}":"{"}
    openbracket = ["(", "[", "{"]
    closedbracket = [")", "]", "}"]
    braces = Stack()
    
    for i in range(len(s1)):
        if s1[i] in openbracket:
            braces.push(s1[i])
        elif s1[i] in closedbracket:
            if braces.isEmpty() == True:
                return False
            if matched[s1[i]] != braces.pop():
                return False
            
    if braces.size() == 0:    
        return True
    
    return False
