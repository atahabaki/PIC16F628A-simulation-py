from pic16f628a import PIC16F628A as PIC

W=0
F=1
sayac=0
K=180

p = PIC()

p.movlw(K)
p.movwf(sayac)
p.nop()
while True:
    p.movlw(2)
    p.subwf(sayac,F)
    p.decfsz(sayac,F)
    if p.skipDECFSZ:
        break
    else:
        p.goto()
        continue

print(f"KCS: {p.KCS}")
