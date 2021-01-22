import unittest
from pic16f628a import PIC16F628A

class TestPIC16F628A(unittest.TestCase):

    def setUp(self):
        self.pic16f628a = PIC16F628A()

    def test_movf(self):
        self.assertEqual(self.pic16f628a.movf(0,1),32)
        self.assertEqual(self.pic16f628a.movf(1,1),33)
        self.assertEqual(self.pic16f628a.movf(2,1),34)
        self.assertEqual(self.pic16f628a.movf(3,1),35)
        self.assertEqual(self.pic16f628a.movf(4,1),36)

    def test_movlw(self):
        self.assertEqual(self.pic16f628a.movlw(32),32)
        self.assertEqual(self.pic16f628a.Accumulator.bits,32)
        self.assertEqual(self.pic16f628a.movlw(255),255)
        self.assertEqual(self.pic16f628a.Accumulator.bits,255)
        self.assertEqual(self.pic16f628a.movlw(132),132)
        self.assertEqual(self.pic16f628a.Accumulator.bits,132)

    def test_movwf(self):
        self.assertEqual(self.pic16f628a.movwf(0),self.pic16f628a.RAM[0].bits)
        self.assertEqual(self.pic16f628a.RAM[0].bits,self.pic16f628a.RAM[0].bits)

    def test_addwf(self):
        self.pic16f628a.movlw(141)
        self.pic16f628a.addwf(0,0)
        self.assertEqual(self.pic16f628a.RAM[0].bits,32)
        self.assertEqual(self.pic16f628a.Accumulator.bits,173)
        self.pic16f628a.addwf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits,205)
        self.assertEqual(self.pic16f628a.Accumulator.bits,173)
        self.pic16f628a.addwf(1,0)
        self.assertEqual(self.pic16f628a.RAM[1].bits,33)
        self.assertEqual(self.pic16f628a.Accumulator.bits,206)
        self.pic16f628a.addwf(1,1)
        self.assertEqual(self.pic16f628a.RAM[1].bits,239)
        self.assertEqual(self.pic16f628a.Accumulator.bits,206)
        self.pic16f628a.addwf(2,0)
        self.assertEqual(self.pic16f628a.RAM[2].bits,34)
        self.assertEqual(self.pic16f628a.Accumulator.bits,240)
        self.pic16f628a.addwf(2,1)
        self.assertEqual(self.pic16f628a.RAM[2].bits,18)
        self.assertEqual(self.pic16f628a.Accumulator.bits,240)

    def test_addlw(self):
        self.pic16f628a.addlw(280)
        self.assertEqual(self.pic16f628a.Accumulator.bits,24)
        self.pic16f628a.addlw(280)
        self.assertEqual(self.pic16f628a.Accumulator.bits,48)
        self.pic16f628a.addlw(3)
        self.assertEqual(self.pic16f628a.Accumulator.bits,51)

    def test_subwf(self):
        self.pic16f628a.movlw(10)
        self.pic16f628a.subwf(0,0)
        self.assertEqual(self.pic16f628a.Accumulator.bits,22)
        self.assertEqual(self.pic16f628a.RAM[0].bits,32)
        self.pic16f628a.subwf(0,1)
        self.assertEqual(self.pic16f628a.Accumulator.bits,22)
        self.assertEqual(self.pic16f628a.RAM[0].bits,10)
        self.pic16f628a.movlw(35)
        self.pic16f628a.subwf(1,0)
        self.assertEqual(self.pic16f628a.Accumulator.bits,254)
        self.assertEqual(self.pic16f628a.RAM[1].bits,33)
        self.pic16f628a.subwf(1,1)
        self.assertEqual(self.pic16f628a.Accumulator.bits,254)
        self.assertEqual(self.pic16f628a.RAM[1].bits,35)

if __name__ == "__main__":
    unittest.main()
