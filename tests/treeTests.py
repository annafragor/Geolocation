import unittest
from src.centeredIntervalTree import CenteredIntervalTree
from locate import read_file
from src.interval import Interval
import os


class TestTreeMethods(unittest.TestCase):
    def test_find_location(self):
        # открытие файла с валидными данными, и поиск в дереве, сформированном на их основе
        path = os.path.realpath(__file__)[:-len('treeTests.py')] + 'filesToRead/inputForTree.txt'
        data = read_file(path)
        control_point1 = data['point']
        intervals1 = data['intervals']
        tree1 = CenteredIntervalTree(intervals1)
        self.assertEqual(tree1.find_location(control_point1), Interval(0, 5, 5))

        # открытие файла с валидными данными, и поиск в дереве, в котором все интервалы покрывают контрольную точку
        path = os.path.realpath(__file__)[:-len('treeTests.py')] + 'filesToRead/inputForTree2.txt'
        data = read_file(path)
        control_point1 = data['point']
        intervals1 = data['intervals']
        tree1 = CenteredIntervalTree(intervals1)
        self.assertEqual(tree1.find_location(control_point1), Interval(0, 2, 7))

        # открытие файла с валидными данными, и поиск элемента, которого в дереве нет
        path = os.path.realpath(__file__)[:-len('treeTests.py')] + 'filesToRead/inputForTree3.txt'
        data = read_file(path)
        control_point1 = data['point']
        intervals1 = data['intervals']
        tree1 = CenteredIntervalTree(intervals1)
        self.assertEqual(tree1.find_location(control_point1), None)



if __name__ == '__main__':
    unittest.main()
