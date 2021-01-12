from logger import Logger as log

class FileRegister:
    """
    A class used to simulate a FileRegister of an PIC16F628A.

    Attributes
    ----------

    bits : list
        Holds information, 8-bit array.
        Contains only 0 and 1 in this list.

    Methods
    -------
    assign_bits(bits=list)
        Assigns bits to the bits one by one.

    assign_bit(bit=int,index=int)
        Changes the bit at given index, bits list should be changed.

    clear_all()
        Resets all bits to 0.

    set_all()
        Sets all bits to 1.
    """


    def __init__(self,bits=[0,0,0,0,0,0,0,0],name="Accumulator"):
        """
        Parameters
        ----------

        bits: list
            Holds information, an array of ints.
            Should contain only 0s and 1s.
        """
        self.name=name
        self.__logger = log(name=self.name)
        self.__clear_bit = 0
        self.__set_bit = 1
        self.__len=8
        if len(bits) == self.__len:
            self.bits=bits
        else:
            self.__logger.warn("__init__",f"The length of the bits should be {self.__len}.")

    def to_int(self):
        """
        Returns corresponding integer value of the bits.
        """
        toplam=0
        for i,val in enumerate(self.bits[::-1]):
            toplam+=(2**i)*val
        return toplam

    def clear_all(self):
        """
        Assign every cell to 0.
        """
        for i in self.bits:
            i = self.__clear_bit
            self.__logger.debug("clear_all",f"{i} is set to 0, cleared in another words.")

    def set_all(self):
        """
        Assign every cell to 1.
        """
        for i in self.bits:
            i = self.__set_bit
            self.__logger.debug("set_all",f"{i} is set to 1, set in another words.")

    def assign_bit(self,bit=0,index=0):
        """
        Change the bit to the given index.

        Parameters
        ----------
        bit: int
            0 or 1
        index: int
            should be between 0-7 (0 and 7 is included.)
        """
        self.bits[index] = bit
        self.__logger.debug("assign_bit",f"bit changed stored at index {index} to {bit}")
    
    def assign_bits(self,bits=[0,0,0,0,0,0,0,0]):
        """
        Changes the bits.

        Parameters
        ----------
        bits: list
            change the array.
        """
        if len(bits) == self.__len:
            self.bits=bits
            self.__logger.debug("assign_bit",f"The bits changed to {bits}.")
        else:
            self.__logger.debug("assign_bits","The length of the bits should be {self.__len}.")
