from arrays import Array, Array2D, DynamicArray
import unittest


class ArrayTest(unittest.TestCase):
    '''class for arrays classes testing'''
    def test_array(self):
        '''Testing array class'''
        arr = Array(100)

        self.assertIsInstance(arr, Array)
        self.assertEqual(arr._size, 100)
        self.assertEqual(len(arr), 100)
        
        arr[0] = 'green'
        self.assertEqual(arr[0], 'green')

        arr.clear('red')
        self.assertEqual(arr[0], 'red')

    def test_dynamic_array(self):
        '''Testing dynamic array class'''
        arr = DynamicArray()

        self.assertIsInstance(arr, DynamicArray)
        self.assertEqual(arr._size, 0)
        self.assertEqual(len(arr), 0)
        
        arr.append('green')
        arr.append('green')
        self.assertEqual(arr[0], 'green')

        arr.remove('green')
        self.assertEqual(arr._size, 1)

    def test_2D_array(self):
        '''Testing 2D array class'''
        arr = Array2D(10, 5)

        self.assertIsInstance(arr, Array2D)
        self.assertEqual(arr.num_rows(), 10)
        self.assertEqual(arr.num_cols(), 5)
        
        arr[(0, 0)] = 'green'
        self.assertEqual(arr[(0, 0)], 'green')

        arr.clear('red')
        self.assertEqual(arr[(0, 0)], 'red')    


if __name__ == "__main__":
    unittest.main()