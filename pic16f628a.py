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

    StatusFileRegister = FileRegister(name="StatusFileRegister")
    Accumulator = FileRegister()
    RAM = []

    def __init__(self):
        pass

    def movf(self,f,d):
        
        pass

    def movwf(self,f):
        pass

    def movlw(self,k):
        pass

