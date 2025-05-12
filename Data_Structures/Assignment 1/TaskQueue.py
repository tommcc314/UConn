# from Task.py import the Task class
from Task import Task

# The class TaskQueue is like a LL. A circular data structure with attributes:
class TaskQueue:
    def __init__(self, time_per_task=1):
        self.current = None  # the current task to process
        self.tail = None
        self.size = 0
        self.used_Id = {}
        self.time_per_task = time_per_task
        # the amount of time to dedicate to each task before moving to the next one.
        # This has a default value of 1, but should be a parameter a user can specify
        # when creating a TaskQueue.

    def add_task(self, newestTaskNode):
        # adds a task immediately before current. Should be O(1).
        # because a task should be added before current, a Linked List with
        # a prev pointer (and also a next pointer) should be used
        # changing the pointers. O(1)

        # if head and tail are None, create first task node, set current and tail to that node
        if self.current is None and self.tail is None:
            newestTaskNode.next = newestTaskNode
            newestTaskNode.prev = newestTaskNode
            self.current = newestTaskNode
            self.tail = newestTaskNode
        # if there is only one TaskNode, set new node as tail and set prev and next to the other node of the pair
        elif self.size == 1:
            newestTaskNode.prev = self.current
            newestTaskNode.next = self.current
            self.tail = newestTaskNode
            self.current.prev = self.tail
            self.current.next = self.tail
        # if it is not any of the 2 above cases, there are 2+ nodes. Set the new node to be the new tail and place it
        # in between the previous tail and current by changing pointers
        else:
            newestTaskNode.prev = self.tail
            newestTaskNode.next = self.current
            self.tail.next = newestTaskNode
            self.tail = newestTaskNode
            self.current.prev = self.tail

        #increase size by 1 and add ID to searchable dictionary
        self.size += 1
        self.used_Id[newestTaskNode.id] = newestTaskNode.id

    def remove_task(self, deleteId):
        # removes the task with a given id. Should be O(n).
        # If a user tries to remove a task with an id that is not in the TaskQueue,
        # you should raise a RuntimeError with an appropriate string.
        #    - This check should run in O(1). Think - what data structure can you use that allows
        #    - O(1) membership testing? – Test this behavior. (The error, not the running time)
        if deleteId not in self.used_Id.keys():
            raise RuntimeError(f'Task with Id {deleteId} was not found in the Task Queue.')
        #if only one element, reset queue
        if self.size == 1:
            self.current = None
            self.tail = None
        #if two elements, remaining element will be current which points to itself
        elif self.size == 2:
            if self.current.id == deleteId:
                self.tail.prev = self.tail
                self.tail.next = self.tail
                self.current = self.tail
            else:
                self.current.prev = self.current
                self.current.next = self.current
                self.tail = self.current

        else:
            if self.current.id == deleteId:
                #set current to be next element and connect tail and new current
                self.current = self.current.next
                self.current.prev = self.tail
                self.tail.next = self.current
            elif self.tail.id == deleteId:
                #set tail to be the previous element and connect new tail and current
                self.tail = self.tail.prev
                self.tail.next = self.current
                self.current.prev = self.tail
            else:
                #cycle through each node until node with id is found.
                #then, set the previous and next node's pointers to point to each other.
                self.current_test = self.current.next
                while self.current_test.id != self.tail.id:
                    if self.current_test.id == deleteId:
                        self.current_test.prev.next = self.current_test.next
                        self.current_test.next.prev = self.current_test.prev
                        break
                    current_test = self.current_test.next
                    continue
        #remove id from dictionary, reduce size
        del self.used_Id[deleteId]
        self.size -= 1
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def execute_tasks(self):
        # executes tasks cyclically. Each task will run for time_per_task or the amount of time
        # it has remaining, whichever is lower. This should print out information whenever a task
        # is finished (see examples for string formatting). At the end, return the total time it took
        # to execute all tasks. You do not need to test the print outs but should test the return value.
        # See next page for class diagrams.

        #create variable to track which node is being executed
        tempTaskNode = self.current
        #accumulators for printed output and total time to be returned
        execute_tasks_output = []
        totaltime = 0

        while self.__len__() != 0:
            #calculate how much time to dedicate to task, reduce the node's time
            runtime = min(self.time_per_task, tempTaskNode.time_left)
            totaltime += runtime
            tempTaskNode.reduce_time(runtime)
            #once task's time is 0, add output string to accumulator list and remove the task
            if tempTaskNode.time_left == 0:
                execute_tasks_output.append(f'Finished task {tempTaskNode.id} at t = {totaltime} seconds')
                self.remove_task(tempTaskNode.id)
            #move to next element
            tempTaskNode = tempTaskNode.next
        for i in execute_tasks_output:
            print(i)
        print("time =", totaltime)
        return totaltime
