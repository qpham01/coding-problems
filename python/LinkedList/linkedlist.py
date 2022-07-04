from tkinter import N


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            nodesCopy = nodes.copy()
            node = LinkedNode(data=nodesCopy.pop(0))
            self.head = node
            for elem in nodesCopy:
                node.next = LinkedNode(data=elem)
                node = node.next  
            self.tail = node    
      
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def value_list(self):
        values = []
        for node in self:
            values.append(node.data)
        return values
    
    def reverse(self):
        node = self.head
        prev_node = None
        self.tail = None
        while node is not None:
            temp = node.next        
            node.next = prev_node
            prev_node = node
            if self.tail is None:
                self.tail = node
            node = temp
        self.head = prev_node                

def test_constructor(values:list):
    llist = LinkedList(values)
    assert llist.head.data == values[0]
    assert llist.tail.data == values[len(values) - 1]
                                    
def test_repr():            
    llist = LinkedList(["a", "b", "c", "d", "e"])
    print(llist)

def test_iter(values:list):
    llist = LinkedList(values)
    i = 0
    for node in llist:
        assert values[i] == node.data
        i += 1

def test_value_list(data: list):
    llist = LinkedList(data)
    result = llist.value_list()
    assert result == data

def test_reverse(data: list, head, tail):
    llist = LinkedList(data)
    data.reverse()
    llist.reverse()
    values = llist.value_list()
    assert values == data
    assert llist.head.data == head
    assert llist.tail.data == tail
    
test_constructor([1, 2, 3, 4, 5])   
test_constructor([1])   
test_constructor(['a', 'b', 'c'])   
test_repr()
test_iter([1, 2, 3, 4, 5])
test_value_list([1, 2, 3, 4, 5])
test_reverse([1, 2, 3, 4, 5], 5, 1)
test_reverse([1, 2], 2, 1)
test_reverse([5], 5, 5)