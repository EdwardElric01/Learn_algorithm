
import numpy as np

class PrioQueueError(ValueError):
    pass

class PrioQueue:
    """
    Implementing priority queues using heaps
    """


    def __init__(self, elist=[]):
        self._elems = list(elist)
        if self._elems != []:
            self.buildheap()


    def is_empty(self):
        return self._elems == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        else:
            return self._elems[0]

    def enqueue(self, e):
        self._elems.append(e)
        self.siftup()

    def siftup(self):
        i = len(self._elems) - 1
        father_i = (i - 1) // 2
        while i > 0 and self._elems[i] < self._elems[father_i]:
            self._elems[i], self._elems[father_i] = self._elems[father_i], self._elems[i]
            i, father_i =  father_i, (i - 1) // 2

    def len(self):
        return len(self._elems)

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('No elements to dequeue')
        else:
            val = self._elems[0]
            if len(self._elems) >= 2:
                self._elems[0] = self._elems.pop()
                self.siftdown(0, len(self._elems)-1)
            else:
                self._elems.pop()
            return val


    def siftdown(self, start, end):
        if self.is_empty():
            return
        else:
            i, j = start, start * 2 - 1
            while j <= end:
                if j + 1 <= end and self._elems[j+1] > self._elems[j]:
                    j = j + 1
                if self._elems[j] < self._elems[i]:
                    self._elems[j] , self._elems[i] = self._elems[i], self._elems[j]
                    i, j = j, j * 2 + 1
                else:
                    break

    def buildheap(self):

        i = 0
        end = len(self._elems)
        for
        while i:
            father = (end - 1) // (2 ** (i+1))
            self.siftup(father, )










    def __str__(self):
        return str(self._elems)






def testPriQueue():
    queue = PrioQueue()
    for i in range(10):
        queue.enqueue(
            int(np.random.normal(scale=1000))
        )
        print(queue)
        print(np.min(queue._elems)==queue.peek())

    for i in range(queue.len()):
        queue.dequeue()
        print(queue)


if __name__ == '__main__':
    testPriQueue()
