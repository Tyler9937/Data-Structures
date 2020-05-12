class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value



    def remove_from_end(self):
        current = self.head
        if not self.head:
            self.head = None
        elif current.get_next() is None:
            return self.head
        else:
            prev = current
            while current.get_next() is not None:
                prev = current
                current = current.get_next()

            prev.next_node = None
            return current.value


# the benchmark test
import time
# import arr q and ll q

n = 100000

start_time = time.time()
for i in range(n):
    pass

end_time = time.time()
