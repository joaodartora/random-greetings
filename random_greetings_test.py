import unittest
import random_greetings

class MyTest(unittest.TestCase):
    def get_random_greeting_with_success(self):
        self.assertEqual(random_greetings.get_random_greeting(), "Boa noite meu Abacaxicultor")

if __name__ == '__main__':
    unittest.main()

