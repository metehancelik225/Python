def karsila(kullaniciAdi):
  print("Hoşgeldiniz, size nasıl yardımcı olabilirim {}?".format(kullaniciAdi))


sys_username1 = "metehan"
sys_password1 = "1234"
sys_username2 = "hakan"
sys_password2 = "2345"

while True:
 kullanici_adi = input("Kullanıcı Adı= ")
 sifre = input("Şifre'yi Giriniz=")

 if kullanici_adi == sys_username1 and  sifre !=sys_password1:
   print("Şifre Yanlış")
 elif kullanici_adi != sys_username1 and sifre == sys_password1:
   ("Kullanıcı Adı Yanlış")
 elif kullanici_adi != sys_username1 and sifre != sys_password1:
   print("Kullanıcı Adı ve Şifre Yanlış")
   
 else:
   print("Giriş Yapıldı! Hoşgeldiniz Sn.Metehan")
   secim = input("Hangi Sayfaya Gitmek İstersiniz? (Ana Sayfa/Bölümler/İletişim/Çıkış):")
   if secim == 'Ana Sayfa':
     print("Ana Sayfaya Yönlendiriliyorsunuz")
   if secim == 'Bölümler':
     print("Bölümler Sayfasına Yönlendiriliyorsunuz")
   if secim == 'İletişim':
     print("İletişim Sayfasına Yönlendiriliyorsunuz")
     print("Telefon No= 05453365623  / Gmail= cmetehan225@gmail.com")
   if secim == 'Çıkış':
     print("Çıkış Yapılıyor....")
     break
