class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes +=1

    def deqeueue(self):
        if self.head is None:
            return None

        deqeueue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -=1
        return deqeueue_node_value

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print("Pass" if (q.size() == 3) else "fail")
q.enqueue("d")
print("Pass" if (q.size() == 4) else "fail")

print("Pass" if (q.deqeueue() == 'a') else "fail")
print("Pass" if (q.deqeueue() == 'd') else "fail")

print("Pass" if (q.size() == 2) else "fail")
