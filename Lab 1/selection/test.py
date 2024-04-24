import unittest
from selection  import selection

class TestSorting(unittest.TestCase):
    def test_sort(self):
        input_data=[11,12,22,25,64] 
        result=selection(input_data)
        self.assertListEqual(input_data,result)
        
if __name__=='__main__':
    unittest.main()


