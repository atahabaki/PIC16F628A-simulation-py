from pic16f628a import PIC16F628A


#FR: 32'den basliyor
sayac_index=0
toplam_index=2
status_index=5
f36=4

W=0
F=1

A=18
B=39

p = PIC16F628A()

p.clrf(toplam_index)
p.movlw(A)
p.movwf(sayac_index)
#cevrim
while True:
    p.movf(sayac_index,W)
    p.addwf(toplam_index,F)
    p.movlw(B)
    p.subwf(sayac_index,W)
    #btfsc = p.skipBTFSC
    #decfsz = p.skipDECFSZ
    #btfss = p.skipBTFSS
    #incfsz = p.skipINCFSZ
    p.btfsc(status_index,2)
    if p.skipBTFSC:
        p.movlw(3)
        p.addwf(sayac_index,F)
        p.goto()
        continue
    else:
        p.goto()
        p.movf(toplam_index,W)
        p.movwf(f36)
        break

print(f"F36: {p.RAM[f36].bits}")
