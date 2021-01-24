from pic16f628a import PIC16F628A

p = PIC16F628A()

p.movlw(49)
p.movwf(0)
p.movlw(107)
p.subwf(0,0)

print("{0:b}".format(p.Accumulator.bits))
