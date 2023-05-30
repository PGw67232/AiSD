class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


class unorderedlist:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


temp = Node(55)
print(temp.getdata())
print(temp.getnext())

mylist = unorderedlist()
mylist.add(32)
mylist.add(52)
mylist.add(25)
mylist.add(35)
mylist.add(73)
mylist.add(12)

print(mylist.size())
print(mylist.search(32))
print(mylist.search(100))
mylist.remove(25)
print(mylist.size())
