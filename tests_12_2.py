import unittest
#import runner_2
import runner_and_tournament as runner_2
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.begun1 = runner_2.Runner('Усейн', 10)
        self.begun2 = runner_2.Runner('Андрей', 9)
        self.begun3 = runner_2.Runner('Ник', 3)


    def tearDownClass(cls):
        print(cls.all_results)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            resultat = {}
            for place, runner in result.items():
                resultat[place] = runner.name
            print(resultat)

    def test_turnir1(self):
        self.turnir1 = runner_2.Tournament(90, self.begun1, self.begun3)
        self.all_results = self.turnir1.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_turnir2(self):
        self.turnir2 = runner_2.Tournament(90, self.begun2, self.begun3)
        self.all_results = self.turnir2.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_turnir3(self):
        self.turnir3 = runner_2.Tournament(90, self.begun1, self.begun2, self.begun3)
        self.all_results = self.turnir3.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()


