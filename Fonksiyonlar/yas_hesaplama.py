def yuz_yasina_kac_yil_var(yas):
    if yas >= 100:
        return "Zaten 100 yaşını geçmişsiniz!"
    else:
        return 100 - yas

# Kullanıcıdan yaş alalım
yas = int(input("Yaşınızı girin: "))
kac_yil_var = yuz_yasina_kac_yil_var(yas)
print(f"100 yaşına ulaşmak için {kac_yil_var} yıl kaldı.")
