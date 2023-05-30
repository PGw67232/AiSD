class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self): #inaczej top - ostatni element
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def sprawdzanie_nawiasow(znak):
    s = Stack()
    czy_poprawny = True
    index = 0
    while index < len(znak) and czy_poprawny:
        a = znak[index]
        if a == "(": s.push(a)
        else:
            if s.size()==0: czy_poprawny=False
            else: s.pop()

        index += 1

    if s.size()==0 and czy_poprawny:
        return True
    else: return False


znak = "((()))"
print(sprawdzanie_nawiasow(znak)) #True

znak2 = "((()))))"
print(sprawdzanie_nawiasow(znak2)) #False