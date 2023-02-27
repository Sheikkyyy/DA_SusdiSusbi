import unittest
import PROJECTCLASS as proj


class testproj(unittest.TestCase):
    def test_dataprocessing(self):
        result = proj(process_data.top3)
        self.assertEqual(result, ' Indonesia ', ' China ', ' Malaysia ')
if _name_ == '_main_':
    unittest.main()