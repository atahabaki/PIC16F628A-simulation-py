from pic16f628a import PIC16F628A

K=78
sayac=0
W=0
F=1

pic=PIC16F628A()

pic.movlw(K)
pic.movwf(sayac)
pic.nop()
while True:
    pic.movlw(2)
    pic.subwf(sayac,F)
    pic.decfsz(sayac,F)
    if pic.skipDECFSZ:
        break
    else:
        pic.goto()
        continue
#goto dongu
print(f"KCS: {pic.KCS}")
