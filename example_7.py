from pic16f628a import PIC16F628A

K=228

W=0
F=1

say1=0
say2=1

p=PIC16F628A()

p.movlw(K)
p.movwf(say1)

skipDon1=False
skipDon2=False

#don1
while not skipDon1:
    p.decf(say1,F)
    p.movlw(K)
    p.movwf(say2)
    #don2
    while not skipDon2:
        p.movlw(2)
        p.subwf(say2,F)
        p.decfsz(say2,F)
        if p.skipDECFSZ:
            p.decfsz(say1,F)
            if p.skipDECFSZ:
                skipDon2=True
                skipDon1=True
            else:
                p.goto()
                continue
        else:
            p.goto()
            continue

print(f"KCS: {p.KCS}")
