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

    change_bit(bit=int,index=int)
        Changes the bit

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
        self.__clear_bits = 0
        self.__set_bits = 255
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

    def get_right_4bits(self):
        return self.bits & 0b00001111

    def get_left_4bits(self):
        return self.bits >> 4

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
            self.__logger.debug("change_bit","Bit should be 0 or 1.")
            return -1

    def ones_complement(self):
        """
        Just changes to 1's complement
        """
        for i in range(0,self.__max_index+1):
            if self.get_bit(i) == 0:
                self.change_bit(1,i)
            elif self.get_bit(i) == 1:
                self.change_bit(0,i)
        return self.bits

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

    def cycle_between_min_and_max(self,bits=0):
        """
        If the bits are bigger than self.__set_bits+1,
        then it subtracts from self.__set_bits+1

        Parameters
        ----------

        bits: int
           Should be between 0-255, if bigger the above sentence/action will do..
        """
        if bits >= self.__set_bits+1:
            self.bits = bits-(self.__set_bits+1)
            if self.bits >= self.__set_bits+1:
                self.bits = self.cycle_between_min_and_max(self.bits)
            return self.bits
        elif bits < 0:
            self.bits = self.__set_bits+1 - abs(bits)
            if self.bits < 0:
                self.bits = self.cycle_between_min_and_max(self.bits)
            return self.bits
        else:
            self.bits = bits
            return bits

    def clear_all(self):
        """
        Replaces all bits to 0s.
        """
        self.bits = self.__clear_bits
        return self.bits

    def set_all(self):
        """
        Replaces all bits to 1s.
        """
        self.bits = self.__set_bits
        return self.bits

    def assign_bits(self,bits=0):
        """
        Not tested.
        """
        if bits >= self.__set_bits+1:
            self.__logger.debug("assign_bits",f"Subtracted from {self.__set_bits+1}.")
            self.bits=self.cycle_between_min_and_max(bits)
        elif bits < self.__clear_bits:
            self.__logger.debug("assign_bits",f"Value is lower than 0... Doing 2's complement...")
            self.bits=self.cycle_between_min_and_max(bits)
        else:
            self.bits=bits
        return self.bits

    def rotate_left(self,carry=0):
        """
        Rotates left the FileRegister.

        Parameters
        ----------

        carry: int
            It's the Carry Flag, and should be 0 or 1
        """
        if carry == 1 or carry == 0:
            self.bits = self.bits << 1
            self.bits=self.change_bit(index=0,bit=carry)
            self.cycle_between_min_and_max(self.bits)
            return self.bits
        else:
            self.__logger.debug("rotate_left","Carry should be 0 or 1.")
            return -1

    def rotate_right(self,carry=0):
        """
        Rotates right the FileRegister.

        Parameters
        ----------

        carry: int
            It's the Carry Flag, and should be 0 or 1
        """
        if carry == 1 or carry == 0:
            self.bits = self.bits >> 1
            self.bits=self.change_bit(index=7,bit=carry)
            self.cycle_between_min_and_max(self.bits)
            return self.bits
        else:
            self.__logger.debug("rotate_right","Carry should be 0 or 1.")
            return -1
