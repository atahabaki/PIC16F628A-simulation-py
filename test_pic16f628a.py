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


if __name__ == "__main__":
    unittest.main()
