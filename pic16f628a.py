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
