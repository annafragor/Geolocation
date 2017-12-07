import unittest
from src.interval import Interval


class TestIntervalMethods(unittest.TestCase):

    def test_is_empty(self):
        # когда часть полей не введена
        self.assertTrue(Interval(1, 2).empty())
        self.assertTrue(Interval(1).empty())
        self.assertTrue(Interval().empty())

        # когда вводятся неверные данные (концы интервала не могут совпадать!)
        self.assertTrue(Interval(2, 2, 3).empty())

        # когда вводятся неверные данные (левый конец не может быть больше правого)
        self.assertTrue(Interval(5, 2, 3).empty())

        # когда все поля введены верно - интервал НЕ пуст
        self.assertFalse(Interval(1, 2, 3).empty())
        self.assertFalse(Interval(1, 2, 0).empty())

    def test_make_empty(self):
        test_interval = Interval(1, 2, 3)  # точно НЕ пустой интервал
        test_interval._make_empty()  # делаем пустым
        self.assertTrue(test_interval.empty())  # становится пустым

    def test_contain_point(self):
        p = 5  # контрольная точка

        # интервал строго левее точки
        self.assertEqual(Interval(-2, 3, 0).contain(5), -1)

        # интервал строго правее точки
        self.assertEqual(Interval(6, 8, 0).contain(5), 1)

        # точка лежит в интервале
        self.assertEqual(Interval(-2, 6, 0).contain(5), 0)

        # точка лежит на левой границе (т.е. лежит в интервале)
        self.assertEqual(Interval(5, 7, 0).contain(5), 0)

        # точка лежит на правой границе (т.е. лежит в интервале)
        self.assertEqual(Interval(-2, 5, 0).contain(5), 0)

    def test_equal_operator(self):
        # одинаковые полные интервалы
        self.assertEqual(Interval(1, 2, 3), Interval(1, 2, 3))

        # пустые интервалы
        self.assertEqual(Interval(1, 2), Interval(1))

        # сравнение полного интервала и НЕ интервала
        self.assertNotEqual(Interval(1, 2, 3), 1)

        # сравнение пустого интервала и None
        self.assertNotEqual(Interval(), None)


if __name__ == '__main__':
    unittest.main()
