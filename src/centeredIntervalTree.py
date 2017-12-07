from src.node import Node


class CenteredIntervalTree:
    def __init__(self, intervals):  # дерево инициализируется массивом интервалов
        self.root = Node(intervals)
        self.size = len(intervals)

    def __str__(self):
        return self.root.__str__()

    def find_location(self, point):
        print('before find')

        result_intervals = self.root.find(point)
        for i in result_intervals:
            print(i)

        print('after find')

        if result_intervals:
            result_location = sorted(result_intervals, key=lambda interval: interval.weight)[-1]
            return result_location
        else:
            return None
