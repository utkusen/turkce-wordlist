Türkçe wordlist çalışmasına kişisel analizlerinizle destek olabilirsiniz.

## Analiz Süreci

- Analiz yapacağınız bilgisayarda Python3 ve pip3 kurulu olduğuna emin olunuz.

- "Parola" ya da "E-posta:Parola" formatında bir veri sızıntısı bulunuz. 

- Proje sayfasından bakarak bu verinin daha önce analiz edilmediğinden emin olun.

- turkce-wordlist reposu içerisinden `corpus.txt`, `arama.py` ve `wordlist.txt` dosyalarını indirin, veri dosyası ile aynı dizine yerleştirin.

- `pip3 install pyahocorasick` komutu ile gerekli kütüphaneyi yükleyin.

- `arama.py` içerisindeki `PAROLA_VERISI.txt` stringini veri dosyanızın ismiyle değiştirin.

- `python3 arama.py > 1.txt` komutu ile analizi başlatın.

- `1.txt` dosyasının içindeki boş satırları yok ederek `wordlist.txt`'ye ekleyin.

- `sort | uniq` komutlarını kullanarak listeyi sıralayın ve tekrarlayan satırları silin.

## Pull Request Süreci

- Pull request gönderirken analiz ettiğiniz veri ile ilgili bilgi vermeyi unutmayın (Nereden sızdı, nereden buldunuz, kaç satır içeriyor gibi)

- Readme dosyasında analiz edilen veriler tablosunu düzenlediğinizden emin olun.