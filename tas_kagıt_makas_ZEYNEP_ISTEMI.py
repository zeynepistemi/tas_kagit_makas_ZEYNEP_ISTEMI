import random
def tas_kagit_makas_ZEYNEP_ISTEMI():
    pass

print("oyuna hoşgeldin")
print("taş makasi kirar, kagit taşi sarar, makas kağidi keser")

kullanici_puan = 0
bilgisayar_puan = 0



while True:
    try:
        kullanici_secimi = int(input("\nTaş: 1"
                                     "\nKagit: 2"
                                     "\nMakas: 3"
                                     "\nHangisini seçmek istiyorsan rakam girin: "))
    except NameError:
        print("Sadece rakam gir canim.")
        continue
    except ValueError:
        print("Sadece rakam gir canim.")
        continue

    if kullanici_secimi not in range(1, 4):
        print("Geçersiz rakam, seçtiğin rakam 1 ve 3'ün arasinda olmali.")
        continue
     
    opsiyonlar = {1: "Taş", 2: "Kagit", 3: "Makas"}
    bilgisayar_secimi = random.randint(1, 3)

    print(f"\nKullanicinin seçimi: {opsiyonlar[kullanici_secimi]} | bilgisayar seçimi: {opsiyonlar[bilgisayar_secimi]}")

    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere!")
    elif kullanici_secimi == 1:
        if bilgisayar_secimi == 2:
            print("bilgisayarin kagidi taşi sardi, bu roundun kazanani bilgisayar!")
            bilgisayar_puan += 10
        elif bilgisayar_secimi == 3:
            print("Oyuncunun taşi bilgisayarin makasini kirdi, oyuncu kazandi!")
            kullanici_puan += 10
    elif kullanici_secimi == 2:
        if bilgisayar_secimi == 1:
            print("Oyuncunun kagidi bilgisayar`in taşini sardi, oyuncu yükseklerde!")
            kullanici_puan += 10
        elif bilgisayar_secimi == 3:
            print("bilgisayarin makasi oyuncunun kagidini kesti, bilgisayar zirvede!")
            bilgisayar_puan += 10
    elif kullanici_secimi == 3:
        if bilgisayar_secimi == 1:
            print("bilgisayarin taşi oyuncunun makasini kirdi, kazanan bilgisayar!")
            bilgisayar_puan += 10
        elif bilgisayar_secimi == 2:
            print("Oyuncunun makasi bilgisayarin kagidini kesti, zirve bu sefer oyuncunun!")
            kullanici_puan += 10

    print(f"\nOyuncunun skoru: {kullanici_puan} | bilgisayarin skoru: {bilgisayar_puan}"
          f"\nTaraflardan birisinin skoru 30'a ulaştiginda oyun biter!")

    if kullanici_puan == 30:
        print("Oyun bitti, kazanan Oyuncu!")
        quit()
    elif bilgisayar_puan == 30:
        print("Oyun bitti, kazanan bilgisayar!")
        devam = input("Tekrar oynayalim mi? Evet ya da Hayir yaz: ").lower()
        if devam == "evet":
            continue
        elif devam == "hayir":
            quit()
        else:
            print("Geçersiz kelime, güle güle...")
            quit()
   

    