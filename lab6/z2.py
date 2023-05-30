# 1. pusty stos
# 2. deklaracja zmiennej bool, oraz index slozaca do przechodzenia po elementach listy
# 3. dopoki index jest mniejszy od size lub do wystapienia 1-go bledu
#   T: odczytaj znak
#      jesli znak jest znakiem otwierajacym dodaj znak na stos,
#   F: sprawdz czy stos jest pusty,
#


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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def sprawdzenie(s):
    stack = []
    for znak in s:
        if znak in ('(', '{', '['):
            stack.append(znak)
        else:
            if stack and (
                (stack[-1] == '(' and znak == ')')
                or (stack[-1] == '{' and znak == '}')
                or (stack[-1] == '[' and znak == ']')
            ):
                stack.pop()
            else:
                return False
    return not stack


def isValid(linia):
    stack = []
    otwarte = set('([{')
    zamkniete = set(')]}')
    pair = {')': '(', ']': '[', '}': '{'}
    for i in linia:
        if i in otwarte:
            stack.append(i)
            print(stack)
        if i in zamkniete:
            if not stack:
                print(stack)
                return False
            elif stack.pop() != pair[i]:
                print(stack)
                return False
            else:
                print(stack)
                continue
    if not stack:
        return True
    else:
        return False


def simple(linia):
    count = 0
    for i in linia:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


linia = '(((())()))'

if simple(linia):
    print('ok')
else:
    print('nie ok')

# if isValid(linia):
#     print("ok")
# else:
#     print("nie ok")

# if sprawdzenie(linia):
#     print("ok")
# else:
#     print("nie ok")
