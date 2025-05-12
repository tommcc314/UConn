class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class Heap:
    def __init__(self):
        self._heap = []
    def insert(self, item, priority):
        #add entry to the end, then upheap
        self._heap.append(Entry(item, priority))
        self._upheap(len(self._heap) - 1)
        return

    def _upheap(self, i):
        # base case: if at root, end
        if i == 0:
            return
        parent = self._parent(i)
        # if item < parent, swap the item and parent and recurse
        if self._heap[i] < self._heap[parent]:
            self._swap(i, parent)
            return self._upheap(parent)
        return

    def _swap(self, c, p):
        self._heap[c], self._heap[p] = self._heap[p], self._heap[c]

    def findmin(self):
        return self._heap[0].item

    def removemin(self):
        # store min item
        min = self._heap[0].item
        # if only root node, just remove it without calling downheap
        if len(self._heap) == 1:
            self._heap.pop()
            return min
        #swap min with last, then delete the last element
        last = len(self._heap) - 1
        self._swap(0, last)
        self._heap.pop()
        #call downheap starting at root
        self._downheap(0)
        return min


    def _downheap(self, p_idx):
        #if leaf, stop
        #if it has only left child, compare current node with left child
        if self._has_left_child(p_idx) and not self._has_right_child(p_idx):
            left_child = self._left(p_idx)
            if self._heap[p_idx].priority > self._heap[left_child].priority:
                self._swap(p_idx, left_child)
                return self._downheap(left_child)
            return
        # if it has only right child, compare current node with right child
        if self._has_right_child(p_idx) and not self._has_left_child(p_idx):
            right_child = self._right(p_idx)
            if self._heap[p_idx].priority > self._heap[right_child].priority:
                self._swap(p_idx, right_child)
                return self._downheap(right_child)
            return
        # if it has two children, compare current node with both children
        # if current node is not less than both children, swap it with the min of children
        if self._has_right_child(p_idx) and self._has_left_child(p_idx):
            left_child = self._left(p_idx)
            right_child = self._right(p_idx)
            if self._heap[p_idx].priority > self._heap[right_child].priority or self._heap[p_idx].priority > self._heap[left_child].priority:
                if self._heap[left_child].priority < self._heap[right_child].priority:
                    self._swap(p_idx, left_child)
                    return self._downheap(left_child)
                else:
                    self._swap(p_idx, right_child)
                    return self._downheap(right_child)
            return
        return

    def _has_left_child(self, i):
        return self._left(i) < len(self._heap)

    def _has_right_child(self, i):
        return self._right(i) < len(self._heap)

    def _parent(self, i):
        return (i - 1)//2

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

if __name__ == '__main__':

    heap = Heap()
    heap.insert("A", 13)
    heap.insert("B", 2)
    heap.insert("C", 0)
    heap.insert("D", 8)
    heap.insert("E", 1)
    heap.insert("F", 5)
    heap.insert("G", 25)

    print(f"min: {heap.findmin()}")
    heap.removemin()
    heap.removemin()
    for entry in heap._heap:
        print(f"item: {entry.item}", end=" ")
        print(f"priority: {entry.priority}")
    myheap = Heap()
    myheap.insert("H", 3)
    myheap.insert("I", 7)
    myheap.insert("J", 1)
    myheap.insert("K", 6)
    myheap.insert("L", 10)
    myheap.insert("M", 2)
    myheap.insert("N", 12)

    for i in range(len(myheap._heap)):
        print(myheap.removemin())
