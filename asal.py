def asal_mi(sayi,bolen=2):
    if sayi < 2:
        return False
    if bolen * bolen > sayi: # Eğer bölene kadar bölünmediyse asal
        return True
    if sayi % bolen == 0:    # Eğer herhangi bir bölen varsa asal değil
        return False
    return asal_mi(sayi,bolen +1) # Bir sonraki bölene geç 

# Örnek:
print(asal_mi(7))
print(asal_mi(6))
print(asal_mi(97))
     