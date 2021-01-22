from fileregister import FileRegister

class PIC16F628A:
    """
    A class used to simulate PIC16F628A.

    Attributes
    ----------

    StatusFileRegister : FileRegister
        A special File Register which holds valuable informations...

    RAM : FileRegister[]
        A list of FileRegisters acts like RAM in PIC16F628A.

    Accumulator: FileRegister
        It holds value. Used to move data to between FileRegisters...

    Methods
    -------

    movf(f=int,d=int)
        f is the index of a register,
        d is the destination
    """


    def __init__(self):
        """
        Initializes PIC16F628A...
        """
        self.StatusFileRegister = FileRegister(name="StatusFileRegister")
        self.Accumulator = FileRegister()
        self.RAM = [
            FileRegister(name="F32",bits=32),
            FileRegister(name="F33",bits=33),
            FileRegister(name="F34",bits=34),
            FileRegister(name="F35",bits=35),
            FileRegister(name="F36",bits=36)
        ]

    def movf(self,f,d):
        """
        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].bits = self.RAM[f].bits
        elif d == 0:
            self.Accumulator.bits = self.RAM[f].bits
        return self.RAM[f].bits

    def movwf(self,f):
        """
        Parameters
        ----------
        f: int
            Index of a single RAM unit (a fileregister)
        """
        self.RAM[f].bits=self.Accumulator.bits
        return self.Accumulator.bits

    def movlw(self,k):
        """
        Parameters
        ----------
        k: int
            0-255
        """
        self.Accumulator.bits=k
        return self.Accumulator.bits

    # Mathematical

    def addwf(self,f,d):
        """
        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits + self.Accumulator.bits)
            #Status bit should change if the result is zero
            if self.RAM[f].bits == 0:
                self.StatusFileRegister.change_bit(index=2,bit=1)
            else:
                self.StatusFileRegister.change_bit(index=2,bit=0)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits + self.Accumulator.bits)
            #Status bit should change if the result is zero
            if self.Accumulator.bits == 0:
                self.StatusFileRegister.change_bit(index=2,bit=1)
            else:
                self.StatusFileRegister.change_bit(index=2,bit=0)

    def addlw(self,k):
        self.Accumulator.assign_bits(k + self.Accumulator.bits)

    def subwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits - self.Accumulator.bits)
            #Status bit should change if the result is zero
            if self.RAM[f].bits == 0:
                self.StatusFileRegister.change_bit(index=2,bit=1)
            else:
                self.StatusFileRegister.change_bit(index=2,bit=0)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits - self.Accumulator.bits)
            #Status bit should change if the result is zero
            if self.Accumulator.bits == 0:
                self.StatusFileRegister.change_bit(index=2,bit=1)
            else:
                self.StatusFileRegister.change_bit(index=2,bit=0)

    def sublw(self,k):
        self.Accumulator.assign_bits(k - self.Accumulator.bits)

    def incf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits + 1)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits + 1)

    def decf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits-1)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits-1)
    
    # Boolean...

    def andlw(self,k):
        self.Accumulator.assign_bits(k & self.Accumulator.bits)

    def andwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits & self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits & self.Accumulator.bits)

    def iorlw(self,k):
        self.Accumulator.assign_bits(k | self.Accumulator.bits)

    def iorwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits | self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits | self.Accumulator.bits)

    def xorlw(self,k):
        self.Accumulator.assign_bits(k ^ self.Accumulator.bits)

    def xorwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits ^ self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits ^ self.Accumulator.bits)

    def comf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].ones_complement())
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].ones_complement())

    # Misc and other stuff...

    def clrf(self,f):
        self.RAM[f].bits = 0

    def clrw(self):
        self.Accumulator.bits = 0

    def bcf(self,f,b):
        self.RAM[f].change_bit(index=b,bit=0)

    def bsf(self,f,b):
        self.RAM[f].change_bit(index=b,bit=1)

    def rrf(self,f,d):
        if d == 1:
            self.RAM[f].rotate_right()
        elif d == 0:
            self.Accumulator.bits = self.Accumulator.bits << 1

    def rlf(self,f,d):
        if d == 1:
            self.RAM[f].rotate_right()
        elif d == 0:
            self.Accumulator.bits = self.Accumulator.bits >> 1

    def swapf(self,f,d):
        pass

    def retlw(self,k):
        pass

    def nop(self):
        pass

    def btfsc(self,f,b):
        pass

    def btfss(self,f,b):
        if self.RAM[f].get_bit(b) == 1:
            self.skip = True
        else:
            self.skip = False

    def incfsz(self,f,d):
        pass

    def decfsz(self,f,d):
        pass
