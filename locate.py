from src.centeredIntervalTree import CenteredIntervalTree
from src.interval import Interval
import sys
import re


def read_file(filename):
    # test
    parcing_result = {
        'point': None,
        'intervals': []
    }

    try:
        file = open(filename, 'r')

    except:
        print('Wrong path to input file!')
        return None

    line = file.readline()
    match_x = re.match(r'\s*(-?\d+)\s*$', line)

    if match_x:
        parcing_result['point'] = int(match_x.group(0))

    else:
        print('Wrong input format of control point! Rewrite your input file and restart a programm.')
        return None  # неверный формат входных данных, а именно контрольной точки

    line = file.readline()
    while line:
        m = re.match(r'\[\s*(?P<begin_point>(-?\d+))\s*,\s*(?P<end_point>(-?\d+))\]\s+(?P<weight>(-?\d+))', line)
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
    args = sys.argv
    if len(args) == 3:
        input_file = args[1]
        output_file = args[2]
        input_data = read_file(input_file)
        intervals = []

        if input_data:
            control_point = input_data['point']
            intervals = input_data['intervals']

            tree = CenteredIntervalTree(intervals)
            resulting_location = tree.find_location(control_point)
            if resulting_location:
                print_result(output_file,
                             'Control point: {} was found in interval [{}:{}] with weight = {}.'.format(
                                 control_point,
                                 resulting_location.begin_point,
                                 resulting_location.end_point,
                                 resulting_location.weight
                             ))

            else:
                print_result(output_file, 'Control point: {} was not found in input intervals.'.format(control_point))

    else:
        print('Wrong input arguments! You should enter 2 filenames.')

