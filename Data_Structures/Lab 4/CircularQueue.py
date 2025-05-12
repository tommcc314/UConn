class CircularQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """ Creating an empty queue. """
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def first(self):
        """ Return (but do not remove) the first element of the queue. """
        pass

    def dequeue(self):
        " Remove and return the first element of the queue. (FIFO)"
        pass

    def enqueue(self, e):
        pass
