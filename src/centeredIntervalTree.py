from src.node import Node


class CenteredIntervalTree:
    def __init__(self, intervals):  # дерево инициализируется массивом интервалов
        self.root = Node(intervals)

    def __str__(self):
        return self.root.__str__()

    def find_location(self, point):
        result_intervals = self.root.find(point)

        if result_intervals:
            result_location = sorted(result_intervals, key=lambda interval: interval.weight)[-1]
            return result_location
        else:
            return None
