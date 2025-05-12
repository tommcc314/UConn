import unittest
from Node import _Node

class Stack_L:
    def __init__(self):
        self._L = list()    # Composition: the Stack_L class has a List

    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()
        #Raises error when trying to pop from the empty stack

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)


    def isempty(self):
        return len(self._L) == 0

class Queue_L:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        try:
            return self._L.pop(0)
        except:
            print("List is already empty.")
        #Raises error when trying to deque from the empty queue

    def peek(self):
        return self._L[0]


    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self._L) == 0

class Stack_LL:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """ Returns the size of the stack """
        return self._size

    def is_empty(self):
        """ Returns True if the stack is empty"""
        return self._size == 0


    def push(self, element):
        """ Add "element" to the top of the stack """
        self._head = _Node(element, self._head)
        self._size += 1

    def pop(self):
        """ Remove element from the top of the stack """
        self.read_element = self._head._element
        self._head = self._head._next
        self._size -=1
        return self.read_element

    def top(self):
        """ Only read the element and donot remove it. """
        return self._head._element

class Queue_LL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the size of the queue """
        return self._size

    def is_empty(self):
        """ Returns True if the queue is empty"""
        return self._size == 0

    def first(self):
        """ Returns (but do not remove) the first element in the queue """
        return self._head._element

    def enqueue(self, element):
        """ Add "element" to the back of the queue """
        self.newest = _Node(element, None)
        if self._tail == None:
            self._head = self.newest
        self._tail = self.newest
        self._size += 1

    def dequeue(self):
        """ Remove element from the front of the queue """
        read_element = self._head._element
        self._head = self._head._next
        if self._head == None:
            self._tail = None
        self._size -= 1
        return read_element

class TestADT(unittest.TestCase):
    #For each ADT, test several instances of pushing and popping. In particular, test adding multiple elements
    #and see if the pop and dequeue return the appropriate elements.
    def test_stack_L(self):
        L = Stack_L()
        L.push(3)
        self.assertEqual(L.pop(), 3)
        L.push(2)
        L.push("hello")
        self.assertEqual(L.pop(), "hello")
        self.assertEqual(L.peek(), 2)
        self.assertEqual(L.__len__(), 1)
        self.assertEqual(L.isempty(), False)
    def test_stack_LL(self):
        L = Stack_LL()
        L.push(3)
        self.assertEqual(L.pop(), 3)
        L.push(2)
        L.push("hello")
        self.assertEqual(L.pop(), "hello")
        self.assertEqual(L.__len__(), 1)
        self.assertEqual(L.is_empty(), False)
    def test_queue_L(self):
        Q = Queue_L()
        Q.enqueue(3)
        self.assertEqual(Q.dequeue(), 3)
        Q.enqueue(2)
        Q.enqueue("hello")
        self.assertEqual(Q.dequeue(), 2)
        self.assertEqual(Q.__len__(), 1)
        self.assertEqual(Q.isempty(), False)
    def test_queue_LL(self):
        Q = Queue_LL()
        Q.enqueue(3)
        self.assertEqual(Q.dequeue(), 3)
        Q.enqueue(2)
        Q.enqueue("hello")
        self.assertEqual(Q.dequeue(), 2)
        self.assertEqual(Q.__len__(), 1)
        self.assertEqual(Q.is_empty(), False)

if (__name__ == '__main__'):
    unittest.main()


