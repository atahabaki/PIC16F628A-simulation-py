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
        self.pic16f628a.RAM[1].assign_bits(254)
        self.pic16f628a.subwf(1,1)
        self.assertEqual(self.pic16f628a.RAM[1].bits,0)
        self.assertEqual(self.pic16f628a.get_zero_flag(),1)

    def test_sublw(self):
        self.pic16f628a.movlw(10)
        self.pic16f628a.sublw(10)
        self.assertEqual(self.pic16f628a.Accumulator.bits,0)
        self.assertEqual(self.pic16f628a.get_zero_flag(),1)
        self.pic16f628a.sublw(0)
        self.assertEqual(self.pic16f628a.Accumulator.bits,0)
        self.pic16f628a.movlw(35)
        self.pic16f628a.sublw(1)
        self.assertEqual(self.pic16f628a.Accumulator.bits,222)
        self.pic16f628a.sublw(100)
        self.assertEqual(self.pic16f628a.Accumulator.bits,134)

    def test_incf(self):
        self.pic16f628a.RAM[0].assign_bits(255)
        self.pic16f628a.incf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits,0)
        self.pic16f628a.incf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits,1)

    def test_decf(self):
        self.pic16f628a.RAM[0].assign_bits(0)
        self.pic16f628a.decf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits,255)
        self.pic16f628a.decf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits,254)

    def test_andlw(self):
        pass

    def test_andwf(self):
        pass

    def test_iorlw(self):
        pass

    def test_iorwf(self):
        pass

    def test_xorlw(self):
        pass

    def test_xorwf(self):
        pass

    def test_comf(self):
        pass

    def test_clrf(self):
        pass

    def test_clrw(self):
        pass

    def test_bcf(self):
        pass

    def test_bsf(self):
        pass

    def test_rrf(self):
        pass

    def test_rlf(self):
        pass

    def test_swapf(self):
        self.pic16f628a.RAM[0].assign_bits(198)
        self.pic16f628a.swapf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits, 108)
        self.pic16f628a.RAM[0].assign_bits(15)
        self.pic16f628a.swapf(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].bits, 240)

    def test_retlw(self):
        self.pic16f628a.retlw(256)
        self.assertEqual(self.pic16f628a.Accumulator.bits,0)
        self.pic16f628a.retlw(2)
        self.assertEqual(self.pic16f628a.Accumulator.bits,2)

    def test_call(self):
        self.pic16f628a.call()
        self.assertEqual(self.pic16f628a.KCS,2)

    def test_goto(self):
        self.pic16f628a.goto()
        self.assertEqual(self.pic16f628a.KCS,2)

    def test_nop(self):
        self.pic16f628a.nop()
        self.assertEqual(self.pic16f628a.KCS,1)

    def test_btfsc(self):
        self.pic16f628a.btfsc(0,1)
        self.assertEqual(self.pic16f628a.RAM[0].get_bit(1),0)
        self.assertEqual(self.pic16f628a.skipBTFSC,True)
        self.pic16f628a.btfsc(0,5)
        self.assertEqual(self.pic16f628a.RAM[0].get_bit(5),1)
        self.assertEqual(self.pic16f628a.skipBTFSC,False)

    def test_btfss(self):
        self.pic16f628a.btfss(0,5)
        self.assertEqual(self.pic16f628a.skipBTFSS,True)
        self.pic16f628a.btfss(0,4)
        self.assertEqual(self.pic16f628a.skipBTFSS,False)
        pass

    def test_incfsz(self):
        pass

    def test_decfsz(self):
        pass

if __name__ == "__main__":
    unittest.main()
