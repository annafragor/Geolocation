import unittest
from locate import read_file
from src.interval import Interval
import os


class TestFileReadingFunction(unittest.TestCase):
    def test_file_parcing(self):
        path = os.path.realpath(__file__)[:-len('fileReadingTest.py')]

        # чтение из правильно составленного файла
        data_from_file1 = read_file(path + 'filesToRead/correctInput.txt')
        self.assertEqual(data_from_file1['point'], 4)
        self.assertEqual(data_from_file1['intervals'],
                         [
                             Interval(-3, 20, 3),
                             Interval(0, 5, 5),
                             Interval(-8, 1, 2)
                         ])

        # чтение из файла, с частично правильно заполненными данными
        data_from_file2 = read_file(path + 'filesToRead/wrongInput1.txt')
        self.assertEqual(data_from_file2, None)
        data_from_file3 = read_file(path + 'filesToRead/wrongInput2.txt')
        self.assertEqual(data_from_file3, None)


if __name__ == '__main__':
    unittest.main()
