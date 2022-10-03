class Queue:
    def __init__(self):
        self.collection = []

    def enqueue(self, element):
        self.collection.insert(0, element)

    def dequeue(self):
        try:
            self.collection.pop()
        except IndexError:
            print("Queue is already empty")

    def show_queue(self):
        print(self.collection)

    def check_empty(self):
        check = '' if len(self.collection) == 0 else 'not '
        print(f"Queue is {check}empty")


q = Queue()
q.dequeue()  # -> Queue is already empty
q.check_empty()  # -> Queue is empty

q.enqueue(3)
q.enqueue(4)
q.enqueue(18)
q.show_queue()  # -> [18, 4, 3]

q.dequeue()
q.show_queue()  # -> [18, 4] FIFO (First Input - First Output), 3 was first
