from pic16f628a import PIC16F628A

W=0
F=1

fr32_id = 0
fr34_id = 2

pic = PIC16F628A()

pic.clrf(fr32_id)
pic.clrf(fr34_id)

pic.movlw(141)
pic.movwf(fr32_id)
pic.movlw(139)
pic.addwf(fr32_id,W)
pic.movwf(fr34_id)
print(f"32. FR: {pic.RAM[fr32_id].bits}")
print(f"34. FR: {pic.RAM[fr34_id].bits}")
print(f"Accumu: {pic.Accumulator.bits}")
print(f"===============================")
