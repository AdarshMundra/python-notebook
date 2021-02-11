import unittest
import cap

class TestCap(unittest.TestCase):

    def test1(self):
        text = 'python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test2(self):
        text = 'python adarsh'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python Adarsh')
if __name__=='__main__':
    unittest.main()
