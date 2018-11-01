import unittest
import hangman1

class TestHangman(unittest.TestCase):#inherit from TestCase
    def setUp(self):#setUp Method is where the game is run
        self.test_game = hangman1.Hangman()

    def test_guess_letter_Type_Error(self): #Test to check non-char
        self.test_game.guess_letter("#") #Test data
        self.assertEqual(self.test_game.guesses_left,8) #Check to see if guesses_left remains the same

    def test_guess_letter(self): #Test to check normal data x 4
        self.test_game.guess_letter("a") #Test data
        self.assertEqual(self.test_game.letter_row,"a****") #Check if updated game.letter_row should equal a****
        self.assertEqual(self.test_game.guesses_left,7) #Check if guesses_left is decremented
        self.assertFalse(self.test_game.check_win()) #Check if check_win is false

        self.test_game.guess_letter("e")
        self.assertEqual(self.test_game.letter_row,"a***e")

        
        
        #add more checks for when guess_letter = p and then guess_letter = l
        #you should use assertEqual, assertFalse or assertTrue
        
if __name__ == '__main__':
    unittest.main()
    
