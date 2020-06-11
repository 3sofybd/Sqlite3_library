from kütüphane import *

print("""
*****************************
HOŞGELDİNİZ/WELCOME

İşlemler :

1.Mevcut Kitapları Göster

2.Kitap Ekle

3.Kitap Sorgula(Sadece İsim Sorgula)

4.Kitap Sorgula(İsim ve Yayınevi birlikte Sorgula)

5.Kitap Sil

Çıkmak için 'q' ya tıklayın.
""")

kitaphane = Kütüphane()
while True:
    degisken = input("Lütfen herhangi bir işlemi seçiniz.")
    if degisken == "q":
        print("Kütüphane Kapatılıyor...")
        time.sleep(2)
        break
    
    elif degisken == "1":
        kitaphane.kitapları_goster()
    
    elif degisken == "2":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        basım_yılı = int(input("Basım Yılı: "))
        baskı = int(input("Baskı: "))
        sayfa_sayısı = int(input("Sayfa Sayısı: "))
        
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,basım_yılı,baskı,sayfa_sayısı)
        kitaphane.kitap_ekle(yeni_kitap)

    elif degisken == "3":
        isim = input("İsim: ")
        kitaphane.is_kitap_ara(isim)

    elif degisken == "4":
        isim = input("İsim: ")
        yayınevi = input("Yayınevi: ")
        kitaphane.isyay_kitap_ara(isim,yayınevi)

    elif degisken == "5":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        basım_yılı = int(input("Basım Yılı: "))
        baskı = int(input("Baskı: "))
        sayfa_sayısı = int(input("Sayfa Sayısı: "))
        
        silinecek_kitap = Kitap(isim,yazar,yayınevi,tür,basım_yılı,baskı,sayfa_sayısı)
        kitaphane.kitabı_sil(silinecek_kitap)
    
    else:
        print("Geçersiz İşlem Girildi.")    

print("Kütüphane Kapatıldı.")






















































