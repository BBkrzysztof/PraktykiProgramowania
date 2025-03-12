import unittest
from function import Add

class TestAddFunction(unittest.TestCase):
    def test_can_add(self):
        result = Add("1,2")
        self.assertEqual(result, 3)
    
    def test_return_single(self):
        result = Add("4")
        self.assertEqual(result, 4)
    
    def test_return_empty(self):
        result = Add("")
        self.assertEqual(result, 0)

    def test_can_add_more(self):
        result = Add("1,2,3")
        self.assertEqual(result, 6)
    
    def test_accept_end_line(self):
        result = Add("1\n2,3")
        self.assertEqual(result, 6)
    
    def test_accept_end_line(self):
        result = Add("1,\n2,3")
        self.assertEqual(result, -1)
        result = Add("1\n,2,3")
        self.assertEqual(result, -1)

    def test_bad_start_or_end(self):
        result = Add(",1,\n2,3")
        self.assertEqual(result, -1)
        result = Add("1,\n2,3,")
        self.assertEqual(result, -1)
