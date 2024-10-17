import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = runner.Runner('Maxim')
        for i in range(10) :
            test1.walk()
        self.assertEqual(test1.distance, 50)


    def test_run(self):
        test2 = runner.Runner('Maxim')
        for i  in  range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test3 = runner.Runner('Maxim')
        test4 = runner.Runner('Olga')
        for i in range(10) :
            test3.run()
            test4.walk()
        self.assertNotEqual(test3.distance, test4.distance)


if __name__ == '__main__':
    unittest.main()

