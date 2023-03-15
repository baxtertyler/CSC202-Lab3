import unittest
# from queue_array import Queue
from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_num(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        try:
            q.dequeue()
        except IndexError:
            print("empty")
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        q.enqueue(3)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.enqueue(4)
        self.assertEqual(q.size(), 3)
        q.enqueue(5)
        self.assertEqual(q.size(), 4)
        q.dequeue()
        self.assertEqual(q.size(), 3)
        q.enqueue(6)
        self.assertEqual(q.size(), 4)
        q.enqueue(7)
        self.assertEqual(q.size(), 5)
        self.assertTrue(q.is_full())
        try:
            q.enqueue(100)
        except IndexError:
            print("full")
        q.dequeue()
        self.assertEqual(q.size(), 4)
        q.dequeue()
        self.assertEqual(q.size(), 3)
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)

    def test_all(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        try:
            q.dequeue()
        except IndexError:
            print("empty")
        q.enqueue('a')
        self.assertEqual(q.size(), 1)
        q.enqueue(66)
        self.assertEqual(q.size(), 2)
        q.enqueue(True)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.enqueue("hello")
        self.assertEqual(q.size(), 3)
        q.enqueue(5)
        self.assertEqual(q.size(), 4)
        q.dequeue()
        self.assertEqual(q.size(), 3)
        q.enqueue(None)
        self.assertEqual(q.size(), 4)
        q.enqueue(False)
        self.assertEqual(q.size(), 5)
        self.assertTrue(q.is_full())
        try:
            q.enqueue(100)
        except IndexError:
            print("full")
        q.dequeue()
        self.assertEqual(q.size(), 4)
        q.dequeue()
        self.assertEqual(q.size(), 3)
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)


if __name__ == '__main__':
    unittest.main()
