import sqlite3
import time

class Kitap():

    def __init__(self,isim,yazar,yayınevi,tür,basım_yılı,baskı,sayfa_sayısı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.basım_yılı = basım_yılı
        self.baskı = baskı
        self.sayfa_sayısı = sayfa_sayısı

    def __str__(self):
        return "İsim: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBasım Yılı: {}\nBaskı Sayısı: {}. Baskı\nSayfa Sayısı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.basım_yılı,self.baskı,self.sayfa_sayısı)

class Kütüphane():

    def __init__(self):
        self.baglanti = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("create table if not exists kitaplık(isim text,yazar text,yayınevi text,tür text,basım_yılı int,baskı int,sayfa_sayısı int)")
        self.baglanti.commit()

    def kitap_ekle(self,kitap):
        self.cursor.execute("select * from kitaplık where isim = ? and yazar = ? and yayınevi = ? and tür = ? and basım_yılı = ? and baskı = ? and sayfa_sayısı = ?",(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.basım_yılı,kitap.baskı,kitap.sayfa_sayısı))
        liste = self.cursor.fetchall()
        if len(liste)==0:
            self.cursor.execute("insert into kitaplık values(?,?,?,?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.basım_yılı,kitap.baskı,kitap.sayfa_sayısı))
            self.baglanti.commit()
            print("Kitabınız başarıyla eklenmiştir.")
        else :
            print("Özellikleri girilen kitap kütüphanede mevcuttur.")
    
    def kitapları_goster(self):
        self.cursor.execute("select * from kitaplık")
        liste = self.cursor.fetchall()
        if len(liste) != 0:
            print("Mevcut Kİtaplar: ")
            for i in liste:
                kitav = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(kitav)
        else:
            print("Kitaplıkta hiç kitap yok.")

    def kitabı_sil(self,kitap):
        self.cursor.execute("delete from kitaplık where isim = ? and yazar = ? and yayınevi = ? and tür = ? and basım_yılı = ? and baskı = ? and sayfa_sayısı = ?",(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.basım_yılı,kitap.baskı,kitap.sayfa_sayısı))
        self.baglanti.commit()
        print("Kitabınız başarıyla silinmiştir.")

    def isyay_kitap_ara(self,isim,yayınevi):
        self.cursor.execute("select * from kitaplık where isim=? and yayınevi = ?",(isim,yayınevi))
        liste = self.cursor.fetchall()
        if len(liste) != 0 :
            for i in liste:
                kitav = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(kitav)
        else :
            print("Böyle bir kitap bulunamadı")

    def is_kitap_ara(self,isim):
        self.cursor.execute("select * from kitaplık where isim=?",(isim,))
        liste = self.cursor.fetchall()
        if len(liste) != 0 :
            for i in liste:
                kitav = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(kitav)
        else :
            print("Böyle bir kitap bulunamadı")











