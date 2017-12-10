from statistics import median


class Node:
    def __init__(self, intervals=None):
        # begin_sorted_input_intervals = None
        if intervals:
            # intervals = sorted(intervals, key=lambda interval: interval.begin_point)
            self.x_center = self._calculate_x_center(intervals)

        else:
            self.x_center = None

        self.left_int, self.right_int, self.center_intervals = None, None, None
        if not self.x_center is None:
            self.set_intervals(intervals)

    @staticmethod
    def _calculate_x_center(intervals):  # серидина диапазонов всех интервалов
        # test
        if intervals:
            points_arr = []
            for interval in intervals:
                points_arr.append(interval.begin_point)
                points_arr.append(interval.end_point)
            center = median(points_arr)
            # beg_sorted = sorted(intervals, key=lambda interval: interval.begin_point)
            # end_sorted = sorted(intervals, key=lambda interval: interval.end_point)
            # center = (intervals[0].begin_point + end_sorted[-1].end_point) // 2
            return center

        else:
            return None

    def set_intervals(self, begin_sorted_intervals):
        # test
        left_intervals, beg_sorted_center_intervals, right_intervals = [], [], []
        if begin_sorted_intervals:
            for interval in begin_sorted_intervals:
                if interval.contain(self.x_center) < 0:
                    left_intervals.append(interval)

                elif interval.contain(self.x_center) == 0:
                    beg_sorted_center_intervals.append(interval)  # получаются тоже отсортированными по beg_point

                else:
                    right_intervals.append(interval)

        self.left_int = Node(left_intervals)
        self.right_int = Node(right_intervals)
        self.center_intervals = CenterIntervals(beg_sorted_center_intervals)

    def __str__(self):
        node_str = ''
        for elem in [self.left_int, self.center_intervals, self.right_int]:
            node_str = self._intervals_to_str(node_str, elem)

        return node_str[:-2]

    @staticmethod
    def _intervals_to_str(res_string, which_int):
        if which_int:
            string = which_int.__str__()
            if string:
                res_string += string
                res_string += '; '
        return res_string

    def find(self, point):
        # test
        result_intervals = []

        if point == self.x_center:
            return self.center_intervals.begin_sorted

        elif self.x_center and point > self.x_center:
            result_intervals = self._get_from_sorted(point, end_sorted=True)
            if self.right_int:
                result_intervals += self.right_int.find(point)

        elif self.x_center and point < self.x_center:
            result_intervals = self._get_from_sorted(point, end_sorted=False)
            if self.left_int:
                result_intervals += self.left_int.find(point)

        return result_intervals

    def _get_from_sorted(self, point, end_sorted=False):
        res = []
        i = 0

        if end_sorted:
            while i < len(self.center_intervals.end_sorted) and point <= self.center_intervals.end_sorted[
                        -i - 1].end_point:
                if self.center_intervals.end_sorted[-i - 1].contain(point) == 0:
                    res.append(self.center_intervals.end_sorted[-i - 1])
                i += 1

        else:
            while i < len(self.center_intervals.begin_sorted) and point >= self.center_intervals.begin_sorted[
                i].begin_point:

                if self.center_intervals.begin_sorted[i].contain(point) == 0:
                    res.append(self.center_intervals.begin_sorted[i])
                i += 1

        return res


class CenterIntervals:
    def __init__(self, intervals):
        self.begin_sorted = sorted(intervals, key=lambda interval: interval.begin_point)  # по возр
        self.end_sorted = sorted(intervals, key=lambda interval: interval.end_point)

    def __str__(self):
        res = ''
        for interval in self.begin_sorted:
            res += interval.__str__()
            res += ', '
        return res[:-2]
