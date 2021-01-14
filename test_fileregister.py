import unittest
from fileregister import FileRegister

class TestFileRegister(unittest.TestCase):

    def setUp(self):
        self.fr1=FileRegister(bits=13,name="FR1")
        self.fr2=FileRegister(bits=25,name="FR2")
        self.fr3=FileRegister(bits=36,name="FR3")
        self.fr4=FileRegister(bits=67,name="FR4")

    def test_get_bit(self):
        #fr1
        self.assertEqual(self.fr1.get_bit(index=0),1)
        self.assertEqual(self.fr1.get_bit(index=1),0)
        self.assertEqual(self.fr1.get_bit(index=2),1)
        self.assertEqual(self.fr1.get_bit(index=3),1)
        self.assertEqual(self.fr1.get_bit(index=4),0)
        self.assertEqual(self.fr1.get_bit(index=5),0)
        self.assertEqual(self.fr1.get_bit(index=6),0)
        self.assertEqual(self.fr1.get_bit(index=7),0)
        #fr2
        self.assertEqual(self.fr2.get_bit(index=0),1)
        self.assertEqual(self.fr2.get_bit(index=1),0)
        self.assertEqual(self.fr2.get_bit(index=2),0)
        self.assertEqual(self.fr2.get_bit(index=3),1)
        self.assertEqual(self.fr2.get_bit(index=4),1)
        self.assertEqual(self.fr2.get_bit(index=5),0)
        self.assertEqual(self.fr2.get_bit(index=6),0)
        self.assertEqual(self.fr2.get_bit(index=7),0)
        #fr3
        self.assertEqual(self.fr3.get_bit(index=0),0)
        self.assertEqual(self.fr3.get_bit(index=1),0)
        self.assertEqual(self.fr3.get_bit(index=2),1)
        self.assertEqual(self.fr3.get_bit(index=3),0)
        self.assertEqual(self.fr3.get_bit(index=4),0)
        self.assertEqual(self.fr3.get_bit(index=5),1)
        self.assertEqual(self.fr3.get_bit(index=6),0)
        self.assertEqual(self.fr3.get_bit(index=7),0)
        #fr4
        self.assertEqual(self.fr4.get_bit(index=0),1)
        self.assertEqual(self.fr4.get_bit(index=1),1)
        self.assertEqual(self.fr4.get_bit(index=2),0)
        self.assertEqual(self.fr4.get_bit(index=3),0)
        self.assertEqual(self.fr4.get_bit(index=4),0)
        self.assertEqual(self.fr4.get_bit(index=5),0)
        self.assertEqual(self.fr4.get_bit(index=6),1)
        self.assertEqual(self.fr4.get_bit(index=7),0)

    def test_get_bits(self):
        self.assertEqual(self.fr1.get_bits(),'00001101')
        self.assertEqual(self.fr2.get_bits(),'00011001')
        self.assertEqual(self.fr3.get_bits(),'00100100')
        self.assertEqual(self.fr4.get_bits(),'01000011')

    def test_change_bit(self):
        #fr1: 13 fr2: 25 #fr3: 36 fr4: 67
        self.assertEqual(self.fr1.change_bit(1,4),29)
        self.assertEqual(self.fr1.change_bit(0,3),21)
        #fr2: 25
        self.assertEqual(self.fr2.change_bit(0,4),9)
        self.assertEqual(self.fr2.change_bit(1,5),41)
        #fr3: 36
        self.assertEqual(self.fr3.change_bit(1,6),100)
        self.assertEqual(self.fr3.change_bit(0,5),68)
        #fr4: 67
        self.assertEqual(self.fr4.change_bit(1,6),67)
        self.assertEqual(self.fr4.change_bit(0,2),67)

    def test_clear_all(self):
        self.assertEqual(self.fr1.clear_all(),0b00000000)
        self.assertEqual(self.fr2.clear_all(),0b00000000)
        self.assertEqual(self.fr3.clear_all(),0b00000000)
        self.assertEqual(self.fr4.clear_all(),0b00000000)

    def test_set_all(self):
        self.assertEqual(self.fr1.set_all(),0b11111111)
        self.assertEqual(self.fr2.set_all(),0b11111111)
        self.assertEqual(self.fr3.set_all(),0b11111111)
        self.assertEqual(self.fr4.set_all(),0b11111111)
    
if __name__=="__main__":
    unittest.main()
