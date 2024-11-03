# "Простые Юнит-Тесты"
from unittest import TestCase

import unit1
import unittest


class RunnerTest(TestCase):
    def test_walk(self):
        w = unit1.Runner('1')
        for i in range(10):
            w.walk()
        self.assertEqual(w.distance, 50)

    def test_run(self):
        r = unit1.Runner('2')
        for j in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        walk1 = unit1.Runner('3')
        run1 = unit1.Runner('4')
        for k in range(10):
            walk1.walk()
            run1.run()
        self.assertNotEqual(walk1.distance, run1.distance)


if __name__ == "__main__":
    unittest.main()
