from pic16f628a import PIC16F628A

A=15
B=30
W=0
F=1

pic=PIC16F628A()

sayac_id=0
toplam_id=2

sayac = pic.RAM[sayac_id]
toplam = pic.RAM[toplam_id]

pic.clrf(toplam_id)
pic.movlw(A)
pic.movwf(sayac_id)
i = 0
#cevrim
while True:
    pic.movf(sayac_id,W)
    pic.addwf(toplam_id,F)
    pic.movlw(B)
    pic.subwf(sayac_id,W)
    print(f"{i}.Sayac: {sayac.bits}")
    print(f"{i}.Toplam: {toplam.bits}")
    print(f"{i}.36. FR: {pic.RAM[4].bits}\n")
    i+=1
    if pic.StatusFileRegister.get_bit(2) == 0:
        pic.movlw(3)
        pic.addwf(sayac_id,F)
    else:
        #sonuc
        pic.movf(toplam_id,W)
        pic.movwf(4)
        break

print(f"Sayac: {sayac.bits}")
print(f"Toplam: {toplam.bits}")
print(f"36. FR: {pic.RAM[4].bits}")
