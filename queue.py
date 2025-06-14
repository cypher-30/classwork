class CircularQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0


    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]


    def dequeue(self):

        if self.is_empty():
            raise Empty("Queue is empty for dequeue operations")

    def enqueue(self):
        if self._size == len(self._data):
            pass

    def resize(self, new_capacity):
        pass

class Empty(Exception):
    pass
if __name__ == "__main__":
    object_Queue = CircularQueue()
