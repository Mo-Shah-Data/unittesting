import unittest
import unit_testing_sample as uts
import heapq

class TestMethods(unittest.TestCase):

    def test_create_empty_list(self):
        self.assertEqual(uts.create_empty_list(), [])

    def test_add_values_list_and_create_heap(self):
        self.assertEqual(len(uts.add_values_list_and_create_heap()), 9)

    def test_add_to_heap(self):
        self.assertEqual(len(uts.add_to_heap()),10)

    def test_check_heap_for_specific_value(self):
        heap = uts.add_values_list_and_create_heap()
        # heap should contain 1002
        self.assertTrue(1002 in heap)

    def test_check_heap_for_non_value(self):
        with self.assertRaises(AssertionError):
            heap = uts.add_values_list_and_create_heap()
            # heap should contain 1002
            assert 100222 in heap

    def test_heappop(self):  # make sure it pops the smallest value in the heap
        values_list = [1001, 199, 1002, 1003, 10, 12, 200, 1004, 1005]
        heapq.heapify(values_list)
        self.assertEqual(heapq.heappop(values_list), 10)  # 10 is the minimum value here

    def test_heapushpop_happy(self):  # inserts smallest vlaue and then pops smallest value
        values_list = [1001, 199, 1002, 1003, 10, 12, 200, 1004, 1005]
        heapq.heapify(values_list)
        self.assertEqual(heapq.heappushpop(values_list, 1),1)

    def test_heapushpop_edge(self):  # test edge case
        values_list = [1001, 199, 1002, 1003, 0.99, 10, 12, 200, 1004, 1005]
        heapq.heapify(values_list)
        self.assertEqual(heapq.heappushpop(values_list, 1),0.99)

    def test_heapushpop_bad(self):  # test bad case
        with self.assertRaises(AssertionError) as excinfo:
            values_list = [1001, 199, 1002, 1003, 0.99, 10, 12, 200, 1004, 1005]
            heapq.heapify(values_list)
            popped_value = heapq.heappushpop(values_list, 0.1) == 0.99
            self.assertTrue(popped_value)


    def test_heapreplace(self):
        with self.assertRaises(IndexError): #as excinfo:
            values_list = []
            heapq.heapify(values_list)
            heapq.heapreplace(values_list, 10)

if __name__ == '__main__':
    unittest.main()
