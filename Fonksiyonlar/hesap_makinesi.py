def hesap_makinesi(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    if b != 0:
        bolum = a / b
    else:
        bolum = "Bölme hatası (0'a bölünemez)"
    return toplam, fark, carpim, bolum

# Kullanıcıdan input alalım
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
toplam, fark, carpim, bolum = hesap_makinesi(sayi1, sayi2)

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
