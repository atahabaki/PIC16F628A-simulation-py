import unittest
from fileregister import FileRegister

class TestFileRegister(unittest.TestCase):
    
    def setUp(self):
        self.fr0 = FileRegister(bits=[0,0,0,0,0,0,0,0])
        self.fr1 = FileRegister(bits=[0,0,0,0,1,0,1,0])
        self.fr2 = FileRegister(bits=[0,1,0,0,1,0,1,0])
        self.fr3 = FileRegister(bits=[0,1,0,1,1,0,1,0])
        self.fr4 = FileRegister(bits=[1,1,0,0,1,0,1,0])

    def test_to_int(self):
        self.assertEqual(self.fr0.to_int(),0)
        self.assertEqual(self.fr1.to_int(),10)
        self.assertEqual(self.fr2.to_int(),74)
        self.assertEqual(self.fr3.to_int(),90)
        self.assertEqual(self.fr4.to_int(),202)

if __name__=="__main__":
    unittest.main()
