import unittest
from src.interval import Interval
from src.node import Node, CenterIntervals


class TestNodeMethods(unittest.TestCase):
    def test_calculate_x_center(self):
        # непересекающиеся интервалы, весь диапазон == 6
        ints1 = [
            Interval(0, 2, 0),
            Interval(3, 4, 0),
            Interval(5, 6, 0)
        ]
        self.assertEqual(Node()._calculate_x_center(ints1), 3.5)

        # частично пересекающиеся интервалы, весь диапазон == 6
        ints2 = [
            Interval(0, 2, 0),
            Interval(1, 3, 0),
            Interval(4, 6, 0)
        ]
        self.assertEqual(Node()._calculate_x_center(ints2), 2.5)

        # все интервалы покрываются одним, весь диапазон == 21
        ints3 = [
            Interval(0, 21, 0),
            Interval(1, 3, 0),
            Interval(10, 15, 0),
            Interval(12, 17, 0)
        ]
        self.assertEqual(Node()._calculate_x_center(ints3), 11)

    def test_set_intervals(self):
        # Вершина с двумя сыновями
        ints1 = [
            Interval(0, 2, 0),
            Interval(3, 4, 0),
            Interval(5, 6, 0)
        ]
        node1 = Node(ints1)
        self.assertEqual(node1.left_int.center_intervals.begin_sorted,
                         [Interval(0, 2, 0), ])
        self.assertEqual(node1.right_int.center_intervals.begin_sorted,
                         [Interval(5, 6, 0), ])
        self.assertEqual(node1.center_intervals.begin_sorted,
                         [Interval(3, 4, 0), ])

        # Вершина без сыновей
        ints2 = [
            Interval(0, 2, 0),
        ]
        node2 = Node(ints2)
        self.assertEqual(node2.left_int.center_intervals,
                         None)
        self.assertEqual(node2.right_int.center_intervals,
                         None)
        self.assertEqual(node2.center_intervals.begin_sorted,
                         [Interval(0, 2, 0), ])

    def test_get_from_sorted(self):
        node = Node()
        ints = [
            Interval(0, 21, 0),
            Interval(10, 15, 0),
            Interval(1, 3, 0),
            Interval(12, 17, 0),
        ]
        node.center_intervals = CenterIntervals(ints)

        # поиск в массиве, отсортированном по конечной координате
        self.assertEqual(node._get_from_sorted(10, end_sorted=True),
                         [Interval(0, 21, 0), Interval(10, 15, 0)])

        # поиск в массиве, отсортированном по начальной координате
        self.assertEqual(node._get_from_sorted(10, end_sorted=False),
                         [Interval(0, 21, 0), Interval(10, 15, 0)])

        # поиск несуществующей точки
        self.assertEqual(node._get_from_sorted(127, end_sorted=True), [])
        self.assertEqual(node._get_from_sorted(-15, end_sorted=False), [])

    def test_find(self):
        # поиск в непересекающихся интервалах
        ints1 = [
            Interval(0, 2, 0),
            Interval(3, 4, 0),
            Interval(5, 6, 0)
        ]
        node1 = Node(ints1)

        # покрываемая интервалами точка
        self.assertEqual(node1.find(3), [Interval(3, 4, 0), ])
        # не покрываемая интервалами точка
        self.assertEqual(node1.find(12), [])

        # поиск в пересекающихся интервалах
        ints2 = [
            Interval(0, 21, 0),
            Interval(1, 3, 0),
            Interval(10, 15, 0),
            Interval(12, 17, 0)
        ]
        node2 = Node(ints2)

        # точка находится в нескольких интервалах
        self.assertEqual(node2.find(10), [Interval(0, 21, 0), Interval(10, 15, 0)])
        # точка лежит ровно в одном интервале
        self.assertEqual(node2.find(18), [Interval(0, 21, 0), ])
        # точка не лежит ни в одном интервале
        self.assertEqual(node2.find(-6), [])


if __name__ == '__main__':
    unittest.main()
