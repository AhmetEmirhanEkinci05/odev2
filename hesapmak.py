def hesap_makinesi(sayi1,sayi2,islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
         if sayi2 == 0:
            return "Bölme işlemi için ikinci sayi 0 olamaz!"
    return sayi1 / sayi2 

#örnek:
print(hesap_makinesi(28,5,"+"))
print(hesap_makinesi(5,3,"-"))
print(hesap_makinesi(15,9,"*"))
print(hesap_makinesi(625,25,"/"))