import unittest
import PROJECTCLASS as proj

class testtop3(unittest.TestCase):

    def testdataprocessing(self):
        result = proj(self.top3)
        self.assertEqual(result, ' Indonesia ', ' China ', ' Malaysia ')
if _name_ == '_main_':
    unittest.main()