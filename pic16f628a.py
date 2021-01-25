from fileregister import FileRegister
from logger import Logger

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
        self.Accumulator = FileRegister()
        self.__log = Logger("PIC16F628A")
        self.RAM = [
            FileRegister(name="F32",bits=32),
            FileRegister(name="F33",bits=33),
            FileRegister(name="F34",bits=34),
            FileRegister(name="F35",bits=35),
            FileRegister(name="F36",bits=36),
            FileRegister(name="Status",bits=0)
        ]
        self.status_index = 5
        self.StatusFileRegister = self.RAM[5]
        self.KCS=0
        self.skipBTFSS=None
        self.skipBTFSC=None
        self.skipINCFSZ=None
        self.skipDECFSZ=None

    def __increase_KCS(self,inc=1):
        self.KCS+=inc

    def __increase_KCS_if(self,compare_it,which_is_two):
        self.__log.debug("__increase_KCS_if",f"compare: {compare_it}, two: {which_is_two}")
        if compare_it == which_is_two:
            self.__increase_KCS(inc=2)
            return True
        else:
            self.__increase_KCS()
            return False

    def __status_zero_flag(self,compare_it):
        if compare_it == 0:
            self.StatusFileRegister.change_bit(index=2,bit=1)
        else:
            self.StatusFileRegister.change_bit(index=2,bit=0)

    def get_zero_flag(self):
        return self.StatusFileRegister.get_bit(2)

    def goto(self):
        """
        Does nothing except increasing the KCS value.
        """
        self.__increase_KCS(inc=2)

    def call(self):
        """
        Does nothing except increasing the KCS value.
        """
        self.__increase_KCS(inc=2)

    def movf(self,f,d):
        """
        Moves F to W or F.

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
        self.__increase_KCS()
        return self.RAM[f].bits

    def movwf(self,f):
        """
        Parameters
        ----------
        f: int
            Index of a single RAM unit (a fileregister)
        """
        self.RAM[f].bits=self.Accumulator.bits
        self.__increase_KCS()
        return self.Accumulator.bits

    def movlw(self,k):
        """
        Parameters
        ----------
        k: int
            0-255
        """
        self.Accumulator.bits=k
        self.__increase_KCS()
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
            self.__status_zero_flag(self.RAM[f].bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits + self.Accumulator.bits)
            #Status bit should change if the result is zero
            self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def addlw(self,k):
        self.Accumulator.assign_bits(k + self.Accumulator.bits)
        self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def subwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits - self.Accumulator.bits)
            #Status bit should change if the result is zero
            self.__status_zero_flag(self.RAM[f].bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits - self.Accumulator.bits)
            #Status bit should change if the result is zero
            self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def sublw(self,k):
        self.Accumulator.assign_bits(k - self.Accumulator.bits)
        self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def incf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits + 1)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits + 1)
        self.__increase_KCS()

    def decf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits-1)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits-1)
        self.__increase_KCS()
    
    # Boolean...

    def andlw(self,k):
        self.Accumulator.assign_bits(k & self.Accumulator.bits)
        self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def andwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits & self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits & self.Accumulator.bits)
        self.__increase_KCS()

    def iorlw(self,k):
        self.Accumulator.assign_bits(k | self.Accumulator.bits)
        self.__status_zero_flag(self.Accumulator.bits)
        self.__increase_KCS()

    def iorwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits | self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits | self.Accumulator.bits)
        self.__increase_KCS()

    def xorlw(self,k):
        self.Accumulator.assign_bits(k ^ self.Accumulator.bits)
        self.__increase_KCS()

    def xorwf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits ^ self.Accumulator.bits)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits ^ self.Accumulator.bits)
        self.__increase_KCS()

    def comf(self,f,d):
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].ones_complement())
        elif d == 0:
            temp=self.RAM[f].bits
            self.Accumulator.assign_bits(self.RAM[f].ones_complement())
            self.RAM[f].bits=temp
        self.__increase_KCS()

    # Misc and other stuff...

    def clrf(self,f):
        self.RAM[f].bits = 0
        self.__increase_KCS()

    def clrw(self):
        self.Accumulator.bits = 0
        self.__increase_KCS()

    def bcf(self,f,b):
        self.RAM[f].change_bit(index=b,bit=0)
        self.__increase_KCS()

    def bsf(self,f,b):
        self.RAM[f].change_bit(index=b,bit=1)
        self.__increase_KCS()

    def rrf(self,f,d):
        """
        Rotates right and assign_bits to (W) or (f), according to d value.
        
        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].rotate_right()
        elif d == 0:
            self.Accumulator.rotate_right()
        self.__increase_KCS()

    def rlf(self,f,d):
        """
        Rotates left and assign_bits to (W) or (f), according to d value.

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].rotate_left()
        elif d == 0:
            self.Accumulator.rotate_left()
        self.__increase_KCS()

    def swapf(self,f,d):
        """
        Swaps 4 bits between right and left, then assigns to W or F,
        according to d value.

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        left=self.RAM[f].bits & 0b11110000
        right=self.RAM[f].bits & 0b00001111
        left >>= 4
        right <<= 4
        res = left | right
        if d == 0:
            self.Accumulator.assign_bits(res)
        elif d == 1:
            self.RAM[f].assign_bits(res)
        return res

    def retlw(self,k):
        """
        Return with literal (k) to (W) Accumulator.
        Note: Should break the loop, remember to put break after this.
        ----------
        k: int
            The value of k will be assigned to W (Accumulator).
        """
        self.Accumulator.assign_bits(k)
        return k

    def nop(self):
        """
        Does nothing, except increasing KCS value.
        """
        self.__increase_KCS()

    def btfsc(self,f,b):
        """
        Bit test fileregister skip if clear (0).

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        b: int
        """
        self.skipBTFSC = self.__increase_KCS_if(self.RAM[f].get_bit(b),0)

    def btfss(self,f,b):
        """
        Bit test fileregister skip if set (1).

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        b: int
        """
        self.skipBTFSS = self.__increase_KCS_if(self.RAM[f].get_bit(b),1)

    def incfsz(self,f,d):
        """
        Increase the value of F, skip if Zero.

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits+1)
            self.skipINCFSZ = self.__increase_KCS_if(self.RAM[f].bits,0)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits+1)
            self.skipINCFSZ = self.__increase_KCS_if(self.Accumulator.bits,0)

    def decfsz(self,f,d):
        """
        Decrease the value of F, skip if Zero.

        Parameters
        ----------
        f: int
            Index of a single RAM unit (a FileRegister)
        d: int
        """
        if d == 1:
            self.RAM[f].assign_bits(self.RAM[f].bits-1)
            self.skipDECFSZ = self.__increase_KCS_if(self.RAM[f].bits,which_is_two=0)
        elif d == 0:
            self.Accumulator.assign_bits(self.RAM[f].bits-1)
            self.skipDECFSZ = self.__increase_KCS_if(self.Accumulator.bits,which_is_two=0)
