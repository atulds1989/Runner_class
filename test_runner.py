import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        
        # Check the initialization of attributes
        self.assertEqual(runner.name, 'Elijah')
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, 'Australia')
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)


class Test_runner_custom_cases(unittest.TestCase):

    def test_runner_drain_energy(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        self.assertEqual(runner.drain_energy(600), 400)


    def test_runner_recover_energy(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        self.assertEqual(runner.recover_energy(100), 1000)



if __name__ == '__main__':
    unittest.main()

