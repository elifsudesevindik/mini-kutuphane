import os

class kitapp:
    def __init__(self, yazar, ad, sayfa):
        self.yazar = yazar
        self.ad = ad
        self.sayfa = sayfa
    

    def kayit(self):
        self.yazar = input("Yazar adını giriniz: ")
        self.ad = input("Kitap adını giriniz: ")
        
        while True:
            try:
                self.sayfa = int(input("Sayfa sayısını giriniz: "))
                with open("kutuphane.txt", "a") as dosya:
                    dosya.write(f"{self.yazar}, {self.ad}, {self.sayfa}\n")
                print("Kitap kaydedildi.")
                break
            except ValueError:
                print("Lütfen sadece sayı giriniz.")
                
    def ara(self):
        if not os.path.exists("kutuphane.txt"):
            print("henüz hiç kitap kaydı yapılmadı.")
            return
        kelime = input("Aramak istediğiniz kitabın adını veya yazar ismini giriniz: ")
        bulundu = False
        with open("kutuphane.txt", "r") as dosya:
            for satir in dosya:
                if kelime.lower() in satir.lower():
                    print(f"Kitap bulundu: {satir.strip()}")
                    bulundu = True
        if not bulundu:
            print("Kitap bulunamadı.")

    def listele(self):
        if not os.path.exists("kutuphane.txt"):
            print("henüz hiç kitap kaydı yapılmadı.")
            return
        with open("kutuphane.txt", "r") as dosya:
            for satir in dosya:
                print(satir.strip())

    def sil(self):
        if not os.path.exists("kutuphane.txt"):
            print("henüz hiç kitap kaydı yapılmadı.")
            return
        kelime = input("Silmek istediğiniz kitabın adını veya yazar ismini giriniz: ")
        kitaplar = []
        bulundu = False
        with open("kutuphane.txt", "r") as dosya:
            for satir in dosya:
                if kelime.lower() not in satir.lower():
                    kitaplar.append(satir)
                else:
                    bulundu = True
        if bulundu:
            with open("kutuphane.txt", "w") as dosya:
                for kitap in kitaplar:
                    dosya.write(kitap)       
            print(f"{kelime} silindi.")
        else:
            print("Kitap bulunamadı.")
        
    def cikis(self):
        print("Çıkış yapıldı")
        exit()

while True:
    print("1. kitap kaydet" "\n" "2. kitap ara" "\n" "3. kitap sil" "\n" "4. kitap listele" "\n" "5. çıkış")
    try:
        secim = int(input("Seçiminizi yapınız (1-5): "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        continue
    kitap = kitapp("", "", 0)
    
    if secim == 1:
        kitap.kayit()
    elif secim == 2:
        kitap.ara()
    elif secim == 3:
        kitap.sil()
    elif secim == 4:
        kitap.listele()
    elif secim == 5:
        kitap.cikis()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")