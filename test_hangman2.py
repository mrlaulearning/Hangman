import unittest
import hangman2

class TestHangman(unittest.TestCase):
    def setUp(self): #Create two instances of the game
        self.brighton_test_game = hangman2.Hangman("brighton")
        self.bob_test_game = hangman2.Hangman("bob")
          
    def test_long_word_letter_row(self):
        self.assertEqual(self.brighton_test_game.letter_row,"********")#check to see if correct number of asterisk are output

    def test_long_word_guess_letter(self):
        self.assertEqual(self.brighton_test_game.guesses_left,11)
        self.brighton_test_game.guess_letter("b")
        self.assertEqual(self.brighton_test_game.letter_row,"b*******")
        self.assertEqual(self.brighton_test_game.guesses_left,10)#check to see if the guesses is decremented

    #Create a test called test_short_word for the instance of the game called bob_test_game
    #Check if the number of asterix in the letter_row is correct

    #Create a test to check if casting from upper case to lower case works and also check the game win state
        
if __name__ == '__main__':
    unittest.main()
    
