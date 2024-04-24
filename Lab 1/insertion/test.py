import unittest
from insertion  import insertion

class TestSorting(unittest.TestCase):
    def test_sort(self):
        input_data=[12, 11, 13, 5, 6]
        result=insertion(input_data)
        self.assertListEqual(input_data,result)
        
if __name__=='__main__':
    unittest.main()



