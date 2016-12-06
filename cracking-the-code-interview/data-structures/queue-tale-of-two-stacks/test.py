from unittest import TestCase
from unittest import main
from run import MyQueue


class MyQueueTest(TestCase):
    def test_queue_peek_empty(self):
        queue = MyQueue()
        self.assertEqual(queue.peek(), None)

    def test_queue_pop_empty(self):
        queue = MyQueue()
        self.assertEqual(queue.pop(), None)

    def test_queue_put(self):
        queue = MyQueue()
        queue.put(1)
        queue.put(2)
        self.assertEqual(queue.queue, [1, 2])

    def test_queue_pop(self):
        queue = MyQueue()
        queue.put(1)
        queue.put(2)
        queue.put(3)
        self.assertEqual(queue.pop(), 1)

if __name__ == '__main__':
    main()
