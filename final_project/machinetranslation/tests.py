import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    """class docstring"""
    def test1(self):
        self.assertEqual(english_to_french(' '), ' ') # test when null is given as input the output is null.
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french("Yes"), "Oui") # test when Yes is given as input the output is not Oui.
        self.assertEqual(english_to_french("No"), "Non") # test when No is given as input the output is not Non.
        
class Testfrench_to_english(unittest.TestCase): 
    """class docstring"""
    def test1(self):
        self.assertEqual(french_to_english(' '), ' ') # test when null is given as input the output is null.
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english("Oui"), "Yes") # test when Oui is given as input the output is Yes.
        self.assertEqual(french_to_english("Non"), "No") # test when Non is given as input the output is No.
        
unittest.main()