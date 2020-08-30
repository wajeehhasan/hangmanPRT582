import unittest
from hangman_proj import source, randomWord,positionSelector,wordInfo

class TestStringMethods(unittest.TestCase):

    def randomWordSelected(self):
        self.assertIn(randomWord,source,'Word is not in the list')

    def letterPositioningCheck(self):
        self.assertEqual(len(positionSelector('wajeeh')), 3, "positioning failed either removing less or more letters")
    def returnThree(self):
        self.assertTrue(len(wordInfo())==3,'All information is not returned')

if __name__ == '__main__':
    unittest.main()
