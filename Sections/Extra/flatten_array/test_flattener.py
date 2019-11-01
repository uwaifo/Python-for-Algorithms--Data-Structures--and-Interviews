import unittest
from flattener import Flattener

class TestFlattener(unittest.TestCase):
   
    
    def test_flatten(self):
        array_1 = [[1,2,[3]],4]
        self.tester = Flattener()
        self.assertEqual(self.tester.flatten_list(array_1), [1,2,3,4])

if __name__ == "__main__":
    unittest.main()