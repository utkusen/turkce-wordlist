# Bu proje; e-posta adresi, isim, telefon benzeri herhangi bir kişisel veri içermemektedir. Parolalar sadece akademik amaçlarla listelenmektedir. Parolaların gerçek kişilerle ilişkilendirilmesi mümkün değildir.

## Türkçe Wordlist 

Türk kullanıcıların parola seçimlerinin analizi için yapılmış bir çalışmadır. İnternete sızan e-posta ve parola verilerinin içindeki Türkçe kelimelerin tespit edilmesi metodu ile gerçekleştirilmiştir.

Çalışma ile ilgili detaylar için aşağıdaki blog yazılarını okuyabilirsiniz: 

[https://utkusen.com/blog/rockyou-wordlistindeki-turkce-parolalarin-tespiti.html](https://utkusen.com/blog/rockyou-wordlistindeki-turkce-parolalarin-tespiti.html)

[https://utkusen.com/blog/turkce-wordlist-calismasinda-ikinci-faz.html](https://utkusen.com/blog/turkce-wordlist-calismasinda-ikinci-faz.html)

Katkıda bulunmak için `CONTRIBUTING.md` dosyasına göz atabilirsiniz.

### Dosyalar

**wordlist.txt** Tekrarlayan satırların temizlendiği, kullanıma hazır parola listesidir. İki tip parola içerir:

- İçinde Türkçe kelime barındıran parolalar. (Örneğin: `123besiktas123`)

- İçinde Türkçe kelime barındıran e-posta adreslerinin kullandığı parolalar. (Örneğin: `haznedarli92@gmail.com - 38409282`)

Çakışmaların önlenmesi için tüm parolalar küçük harfler ile kaydedilmiştir. Hash kırma saldırılarında Hashcat kuralları kullanılarak çeşitlenme yapılması tavsiye edilir.

**count.txt** En çok kullanılan parolaların listelendiği bir istatistik verisidr.

**corpus.txt** Türkçe kelime derlemidir. Sızan veriler içerisinde burada yer alan kelimeler aranmıştır.

### Katkıda Bulunanlar

Gönüllü desteklerinden ötürü teşekkür ederim:

- Ahmet Külekçi - [https://twitter.com/ahmetskulekci](https://twitter.com/ahmetskulekci)

- Murat Öztürk

- Doğukan Uçak [https://github.com/doggukan](https://github.com/doggukan)


## Analiz Edilen Veriler

| Boyut(byte)      | Dosya İsmi |
| ----------- | ----------- |
| 47803901      | CrackStation's Password Cracking Dictionary       |
| 14979516081      | hashes.org found lists(2012-2020)       |
| 60498886      | rockyou.txt       |
| 32012600   | 1 million PORN COMBO.txt        |
| 34610158      | 1,08M.txt       |
| 53658326      | 1.6M HQ COMBOLIST.txt       |
| 3302774      | 100k mail access.txt       |
| 3270398      | 100K.txt       |
| 3826599      | 110k tr.txt      |
| 430345562      | 13m+.txt       |
| 5287555      | 175k+ fortite combos.txt       |
| 6575617      | 194kgmail_pass.txt       |
| 52936      | 19k.txt       |
| 32902892      | 1m8.7.2020.txt       |
| 30387489      | 1M__EMAIL-PASS_.txt       |
| 6685205      | 200k_gaming.txt       |
| 8994975      | 270k COMBO EMAILPASS.txt       |
| 8574447      | 270k combolist.txt       |
| 153801657      | 4614739.txt       |
| 17401054      | 500k_icloud.txt       |
| 23268967      | 617k.txt       |
| 2145321      | 65k mix mail access.txt       |
| 26108876      | 750k 2.txt       |
| 279520619      | 8.5M COMBOLIST.txt       |
| 29571      | 866 origin combo.txt       |
| 199558028      | 8tracks.txt       |
| 22765299      | 950K Iptv,Sky,Uplay,.txt       |
| 135529445      | Canva_mail_pass.txt       |
| 45876442      | Chronicle.com.txt       |
| 3288601      | combo7234.txt       |
| 930151199      | Combolist30M.txt      |
| 76554486      | Database_2.txt       |
| 14486612      | dubmash.txt       |
| 33120067      | eu 1kk.txt       |
| 53323911      | Fortnite.txt       |
| 1402317106      | imesh.txt       |
| 1076962191      | linkedin.txt       |
| 3249956      | mail access.txt       |
| 1571716864      | myfitnesspal.txt       |
| 739419478      | MyHeritage.com 23kk.txt       |
| 16074200      | Spooky_MIXED_000001.txt       |
| 364328409      | wattpad-emailpass.txt       |
| 1117383516      | Zynga_35.3m_mail_pass.txt      |

## Doğrudan Dahil Edilen Veriler

Aşağıdaki veriler Türkiye kaynaklı platformlardan sızdığı için temizlenip/kırılıp doğrudan wordlist'in içine dahil edilmiştir

| Boyut(byte)      | Dosya İsmi |
| ----------- | ----------- |
| 343352      | 10K BOYNER HİT COMBO.txt       |
| 810354   | 26K TR MailPass.txt        |
| 61209129      | 2M TR COMBOLİST.txt       
| 113345713      | 3M Turkey leaked 2020 Combolist.txt       |
| 254846337      | 7M.txt       |
| 126267      | Trendyoll-MailPass.txt       |
| 6423955      | usermailpas.txt       |
| 1229105      | combo.txt       |
| 27663208      | cilgintavuklar.html       |
| 25544390      | tofisa-uyeler.csv       |
| 5816146      | sochic-uyeler.csv       |
| 106192828      | gezginler.com.sql       |

# Yapılan Araştırmalar

Aşağıdaki araştırmalar Türkçe wordlist projesinden faydalanılarak yapılmıştır.

- Türkiye taraftar sayısı analizi [https://github.com/utkusen/turkce-wordlist/blob/master/analizler/taraftar.md](https://github.com/utkusen/turkce-wordlist/blob/master/analizler/taraftar.md)
