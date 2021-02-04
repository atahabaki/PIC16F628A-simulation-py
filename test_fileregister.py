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

    def test_ones_complement(self):
        self.fr1.ones_complement()
        self.assertEqual(self.fr1.bits,242)

    def test_rotate_left(self):
        #fr1
        self.assertEqual(self.fr1.rotate_left(0),26)
        self.assertEqual(self.fr1.rotate_left(carry=1),53)
        #fr2
        self.assertEqual(self.fr2.rotate_left(1),51)
        self.assertEqual(self.fr2.rotate_left(carry=0),102)
        #fr3
        self.assertEqual(self.fr3.rotate_left(0),72)
        self.assertEqual(self.fr3.rotate_left(0),144)
        self.assertEqual(self.fr3.rotate_left(carry=0),32)
        #fr4
        self.assertEqual(self.fr4.rotate_left(0),134)
        self.assertEqual(self.fr4.rotate_left(carry=1),13)

    def test_rotate_right(self):
        #fr1
        self.assertEqual(self.fr1.rotate_right(0),6)
        self.assertEqual(self.fr1.rotate_right(carry=1),131)
        #fr2
        self.assertEqual(self.fr2.rotate_right(1),140)
        self.assertEqual(self.fr2.rotate_right(carry=0),70)
        #fr3
        self.assertEqual(self.fr3.rotate_right(1),146)
        self.assertEqual(self.fr3.rotate_right(1),201)
        self.assertEqual(self.fr3.rotate_right(carry=1),228)
        self.assertEqual(self.fr3.rotate_right(carry=1),242)
        self.assertEqual(self.fr3.rotate_right(carry=1),249)
        self.assertEqual(self.fr3.rotate_right(carry=1),252)
        self.assertEqual(self.fr3.rotate_right(carry=1),254)
        self.assertEqual(self.fr3.rotate_right(carry=1),255)
        self.assertEqual(self.fr3.rotate_right(carry=1),255)
        #fr4
        self.assertEqual(self.fr4.rotate_right(0),33)
        self.assertEqual(self.fr4.rotate_right(carry=1),144)

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

    def test_cycle_between_min_and_max(self):
        self.assertEqual(self.fr1.cycle_between_min_and_max(280),24)
        self.assertEqual(self.fr2.cycle_between_min_and_max(290),34)
        self.assertEqual(self.fr3.cycle_between_min_and_max(300),44)
        self.assertEqual(self.fr4.cycle_between_min_and_max(255),255)
        self.assertEqual(self.fr4.cycle_between_min_and_max(520),8)

    def test_assign_bits(self):
        self.assertEqual(self.fr1.assign_bits(255),255)
        self.assertEqual(self.fr2.assign_bits(280),24)
        self.assertEqual(self.fr3.assign_bits(283),27)
        self.assertEqual(self.fr4.assign_bits(512),0)
        self.assertEqual(self.fr4.assign_bits(540),28)

    def test_get_right_4bits(self):
        self.assertEqual(self.fr1.get_right_4bits(),13)
        self.assertEqual(self.fr2.get_right_4bits(),9)
        self.assertEqual(self.fr3.get_right_4bits(),4)
        self.assertEqual(self.fr4.get_right_4bits(),3)

    def test_get_left_4bits(self):
        self.assertEqual(self.fr1.get_left_4bits(),0)
        self.assertEqual(self.fr2.get_left_4bits(),1)
        self.assertEqual(self.fr3.get_left_4bits(),2)
        self.assertEqual(self.fr4.get_left_4bits(),4)
    
if __name__=="__main__":
    unittest.main()
