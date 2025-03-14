def palindrom_kontrol(kelime):
    kelime = kelime.lower()  # Küçük harfe çeviriyoruz
    if kelime == kelime[::-1]:  # Kelimenin tersine eşitse palindromdur
        return True
    else:
        return False

# Kullanıcıdan kelime alalım
kelime = input("Bir kelime girin: ")
if palindrom_kontrol(kelime):
    print(f"{kelime} palindromdur.")
else:
    print(f"{kelime} palindrom değildir.")
