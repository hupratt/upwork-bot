import unittest 
from main import UpworkBot

class Test_Upwork_Bot(unittest.TestCase):     
    def test_add(self):          
        self.assertEqual(len(UpworkBot.parse_soup()), 10)

if __name__ == '__main__':
    unittest.main()