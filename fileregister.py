from logger import Logger as log

class FileRegister:
    """
    A class used to simulate a FileRegister of an PIC16F628A.

    Attributes
    ----------

    bits : int
        Holds information, 8-bit array.
        Contains only 0 and 1 in this list.

    Methods
    -------
    assign_bits(bits=int)
        Assigns bits to the bits one by one.

    assign_bit(bit=byte/int,index=int)
        Changes the bit at given index, bits list should be changed.

    get_bit(index=int)
        Returns the bit at given index.

    get_bits()
        Returns the bits in binary form (string).

    clear_all()
        Resets all bits to 0.

    set_all()
        Sets all bits to 1.
    """


    def __init__(self,bits=0,name="Accumulator"):
        """
        Parameters
        ----------

        bits: int
            Holds information, an array of ints.
            Should contain only 0s and 1s.
        name: string
            Name of the fileregister
        """
        self.name=name
        self.__logger = log(name=self.name)
        self.__clear_bits = 0b00000000
        self.__set_bits = 0b11111111
        self.__max_index = 7
        self.assign_bits(bits)

    def __numberAtGivenIndex(self,index=0):
        """
        Just returns 2**(index)

        Parameters
        ----------
        index: int
            It's between 0-7 (0 and 7 included).
        """
        if index > self.__max_index:
            return -1
        return 2**index

    def change_bit(self,bit=0,index=0):
        """
        Changes the bit and returns the bits...

        Parameters
        ----------
        bit: int
            It's 0 or 1
        index: int
            It's between 0-7 (0 and 7 included).
        """
        if bit == 1:
            self.bits = self.bits | self.__numberAtGivenIndex(index)
            return self.bits
        elif bit == 0:
            willand=0
            for i in range(0,self.__max_index+1):
                if i == index:
                    continue
                willand+=self.__numberAtGivenIndex(i)
            self.bits = self.bits & willand
            return self.bits
        else:
            self.__logger.warn("change_bit","Bit should be 0 or 1.")
            return -1

    def get_bit(self,index=0):
        """
        Just returns the bit at given index (indexing should start from 0)

        Parameters
        ----------
        index: int
            It's between 0-7 (0 and 7 included).
        """
        norm=self.__numberAtGivenIndex(index)
        return int((self.bits & norm)/norm)

    def get_bits(self):
        """
        Just returns the bits in binary form...
        """
        bitsstr=""
        for i in range(0,self.__max_index+1)[::-1]:
            bitsstr+=str(self.get_bit(i))
        return bitsstr

    def clear_all(self):
        self.bits = self.__clear_bits
        return self.bits

    def set_all(self):
        self.bits = self.__set_bits
        return self.bits

    def assign_bits(self,bits=0):
        """
        Not tested.
        """
        if bits > self.__set_bits+1:
            self.__logger.warn("assign_bits","Should not be bigger than 256.")
        else:
            self.bits=bits

