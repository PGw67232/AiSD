class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    #zad 1
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #zad 2
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  # jeśli usuwamy pierwszy element
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #zad 4
    def addInOrder(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


#zad 3
def merge(lista1, lista2):
    merged_list = UnorderedList()
    current1 = lista1.head
    current2 = lista2.head

    while current1 is not None and current2 is not None:
        if current1.getData() <= current2.getData():
            merged_list.addInOrder(current1.getData())
            current1 = current1.getNext()
        else:
            merged_list.addInOrder(current2.getData())
            current2 = current2.getNext()

    while current1 is not None:
        merged_list.addInOrder(current1.getData())
        current1 = current1.getNext()

    while current2 is not None:
        merged_list.addInOrder(current2.getData())
        current2 = current2.getNext()

    return merged_list


'''temp = Node(93)
print(temp.getData())
print(temp.getNext())'''

mylist = UnorderedList()
mylist.add(15)
mylist.add(27)
mylist.add(34)
mylist.add(45)
mylist.add(67)
mylist.add(88)

'''print(mylist.size())
print(mylist.search(67))
print(mylist.search(34))'''
mylist.remove(67)

secondlist = UnorderedList()
secondlist.addInOrder(1)
secondlist.addInOrder(55)
secondlist.addInOrder(35)
secondlist.addInOrder(17)

#zlaczona = UnorderedList()
#zlaczona = merge(mylist, secondlist)

current = secondlist.head
while current is not None:
    print(current.getData())
    current = current.getNext()