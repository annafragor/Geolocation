from src.centeredIntervalTree import CenteredIntervalTree
from src.interval import Interval
import re


def read_file(filename):
    # test
    parcing_result = {
        'point': None,
        'intervals': []
    }

    file = open(filename, 'r')
    line = file.readline()
    match_x = re.match(r'\s*(-?\d+)\s*$', line)

    if match_x:
        parcing_result['point'] = int(match_x.group(0))

    else:
        print('Wrong input format of control point! Rewrite your input file and restart a programm.')
        return None  # неверный формат входных данных, а именно контрольной точки

    line = file.readline()
    while line:
        m = re.match(
            r'\[\s*(?P<begin_point>(-?\d+))\s*,\s*(?P<end_point>(-?\d+))\]\s+(?P<weight>(-?\d+))', line)

        if m:
            parcing_result['intervals'].append(Interval(int(m.group('begin_point')),
                                                        int(m.group('end_point')),
                                                        int(m.group('weight'))))

        else:
            print('line "', line[:-1], '" has wrong input format! Rewrite your input file and restart a programm.',
                  sep='')
            return None

        line = file.readline()

    file.close()
    return parcing_result


def print_result(filename, result):
    file = open(filename, 'w')
    file.write(result)
    file.close()


if __name__ == "__main__":
    input_data = read_file('input.txt')
    intervals = []

    if input_data:
        control_point = input_data['point']
        intervals = input_data['intervals']
        print('control point:', control_point)
        tree = CenteredIntervalTree(intervals)
        resulting_location = tree.find_location(control_point)

        if resulting_location:
            print_result('result.txt',
                         'Control point: {} was found in interval [{}:{}] with weight = {}.'.format(
                             control_point,
                             resulting_location.begin_point,
                             resulting_location.end_point,
                             resulting_location.weight
                         ))
        else:
            print_result('result.txt', 'Control point: {} was not found in input intervals.'.format(control_point))
