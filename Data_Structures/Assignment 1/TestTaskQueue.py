import unittest
from TaskQueue import *
# from Task import Task

class TestTaskQueue(unittest.TestCase):
    #test initial state of queue
    def test_init(self):
        circularLL = TaskQueue()
        self.assertEqual(circularLL.current, None)
        self.assertEqual(circularLL.tail, None)
        self.assertEqual(circularLL.size, 0)
        self.assertEqual(circularLL.time_per_task, 1)
        self.assertEqual(circularLL.used_Id, {})

    def test_addtask(self):
        circularLL = TaskQueue()
        circularLL.add_task(Task(1, 1))
        circularLL.add_task(Task(2, 1))
        circularLL.add_task(Task(3, 1))
        #test structure and order of nodes
        self.assertEqual(circularLL.current.id, 1)
        self.assertEqual(circularLL.current.next.id, 2)
        self.assertEqual(circularLL.current.next.next.id, 3)
        self.assertEqual(circularLL.current.next.next.next.id, 1)
        self.assertEqual(circularLL.current.prev.id, 3)
        self.assertEqual(circularLL.current.prev.prev.id, 2)
        self.assertEqual(circularLL.current.prev.prev.prev.id, 1)

    def test_removetask(self):
        circularLL = TaskQueue()
        circularLL.add_task(Task(1, 1))
        circularLL.add_task(Task(2, 1))
        circularLL.add_task(Task(3, 1))
        circularLL.remove_task(2)
        circularLL.remove_task(3)
        self.assertEqual(circularLL.current.id, 1)
        self.assertEqual(circularLL.tail.id, 1)
        # circularLL.remove_task(123123) raises an RuntimeError
        # self.assertRaises(an expected Exception, a function, argument1, argument2, arg etc.)
        self.assertRaises(RuntimeError, circularLL.remove_task, 123123)

    def test_len(self):
        circularLL = TaskQueue()
        circularLL.add_task(Task(1, 1))
        #test size after adding and removing elements
        self.assertEqual(circularLL.__len__(), 1)
        circularLL.add_task(Task(2, 1))
        self.assertEqual(circularLL.__len__(), 2)
        circularLL.remove_task(2)
        self.assertEqual(circularLL.__len__(), 1)

    def test_isempty(self):
        circularLL = TaskQueue()
        #test isempty after adding and removing elements
        self.assertEqual(circularLL.is_empty(), True)
        circularLL.add_task(Task(1, 1))
        self.assertEqual(circularLL.__len__(), 1)
        self.assertEqual(circularLL.is_empty(), False)
        circularLL.remove_task(1)
        self.assertEqual(circularLL.is_empty(), True)

    def test_executetasks(self):
        #use example tasks from assignment and another queue with time_per_task != 1
        circularLL = TaskQueue()
        circularLL.add_task(Task(1, 3))
        circularLL.add_task(Task(2, 1))
        circularLL.add_task(Task(3, 5))
        circularLL.execute_tasks()
        circularLL = TaskQueue(2)
        circularLL.add_task(Task(1, 8))
        circularLL.add_task(Task(2, 5))
        circularLL.add_task(Task(3, 4))
        circularLL.execute_tasks()

if __name__ == '__main__':
    unittest.main()