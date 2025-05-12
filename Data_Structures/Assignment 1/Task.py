# The class Task is like a Node
# Task - a task for the operating system to complete.
# Each task has the following attributes, in addition to any “linking” attributes (like next or prev)
# you decide are necessary:
class Task:
    def __init__(self, id, time_left):
        self.id = id  # self.id is a unique identifier (an int)
        self.time_left = time_left  # self.time_left is the amount of time necessary to complete this task
        self.prev = None
        self.next = None

    # reduce_time(self) reduces time_left by the appropriate amount
    def reduce_time(self, reduce):
        self.time_left -= reduce
