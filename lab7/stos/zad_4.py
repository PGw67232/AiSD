class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def size(self):
        return len(self.items)

def onp(dzialanie):
    s = Stack()
    for a in dzialanie:
        if a.isdigit(): s.push(int(a))
        else:
            liczba2 = s.pop()
            liczba1 = s.pop()
            if a=="+":
                wynik = liczba1 + liczba2
            elif a=="-":
                wynik = liczba1 - liczba2
            elif a=="*":
                wynik = liczba1 * liczba2
            elif a=="/":
                wynik = liczba1 / liczba2
            elif a=="^":
                wynik = liczba1 ** liczba2
            s.push(wynik)
    return s.pop()

d = "73+52-2^*="
print(onp(d))