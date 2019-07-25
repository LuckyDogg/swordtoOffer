class QueueByStack:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def queue_insert(self, one):
        self._stack1.append(one)

    def queue_pop(self):
        if len(self._stack1) == 0 and len(self._stack2) == 0:
            return self.__str__()

        elif len(self._stack2) == 0:
            while len(self._stack1) > 0:
                self._stack2.append(self._stack1.pop())
            return self._stack2.pop()
        else:
            return self._stack2.pop()

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def __str__(self):
        return QueueByStack.__name__ + "'s len is " + str(self.__len__())


if __name__ == '__main__':
    test_queue = QueueByStack()
    queue = [1, 2, 3, 4, 5]
    for i in queue:
        test_queue.queue_insert(i)
    while len(test_queue) > 0:
        test_queue.queue_pop()
    print(test_queue.queue_pop())










