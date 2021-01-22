from pic16f628a import PIC16F628A

K=199
sayac=0
W=0
F=1
KCS=0

pic=PIC16F628A()

pic.movlw(K)
pic.movwf(sayac)
pic.nop()
pic.decf(sayac,F)
while True:
    pic.decf(sayac,F)
    pic.decfsz(sayac,F)
    if pic.skipDECFSZ:
        break
    else:
        #shitty comment
        #remember to put def.goto() before continue
        pic.goto()
        continue
#goto dongu
print(f"KCS: {pic.KCS}")

