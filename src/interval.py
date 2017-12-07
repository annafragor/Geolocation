class Interval:
    def __init__(self, begin_inp=None, end_inp=None, weight_inp=None):
        if begin_inp is None or end_inp is None or weight_inp is None:
            print('You can initialize an Interval only when all fields are real! - ',
                  '[', begin_inp, ', ', end_inp, '] ', weight_inp)
            self._make_empty()

        elif begin_inp >= end_inp:
            print('You can\'t initialize an Interval with begin_point >= end_point! - ',
                  '[', begin_inp, ', ', end_inp, '] ', weight_inp)
            self._make_empty()

        else:
            self.begin_point = begin_inp
            self.end_point = end_inp
            self.weight = weight_inp

    def __str__(self):  # для вызова в print
        return '[{a}, {b}] {c}'.format(a=self.begin_point, b=self.end_point, c=self.weight)

    def __eq__(self, other):
        # test
        if isinstance(other, Interval) and other:
            return (self.begin_point == other.begin_point) and \
                   (self.end_point == other.end_point) and \
                   (self.weight == other.weight)
        return False

    def _make_empty(self):
        # tests
        self.begin_point = None
        self.end_point = None
        self.weight = None

    def empty(self):
        # tests
        return not (self.begin_point or self.end_point or self.weight)

    def contain(self, point):
        # tests
        if point > self.end_point:
            return -1
        elif point < self.begin_point:
            return 1
        return 0
