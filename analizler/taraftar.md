`count.txt` dosyasında yer alan istatistikler üzerinden Türkiye'deki futbol kulüp taraftarlarının oranını çıkarmaya yönelik bir çalışmayı konu almaktadır.

### Kulüpler ve Anahtar Kelimeleri

**kulup**|**anahtar kelime**
:-----:|:-----:
galatasaray| galatasaray cimbom 1905 ultraslan
fenerbahce| fenerbahce fener kanarya 1907 gencfb
besiktas|besiktas karakartal 1903 carsi
trabzonspor|trabzonspor 1967 1461
bursaspor|bursaspor teksas
eskisehir|eskisehir eses
karsiyaka|karsiyaka ksk1912
goztepe|goztepe gozgoz
samsunspor|samsunspor
ankaragucu|ankaragucu gecekondu
sivasspor|sivasspor yigido
konyaspor|konyaspor
adanaspor|adanaspor turbeyler
sakaryaspor|sakaryaspor tatanga
altay|altay
kayserispor|kayserispor
kocaelispor|kocaelispor hodrimeydan
denizli|denizlispor
antalyaspor|antalyaspor
malatyaspor|malatyaspor
kasimpasa|kasimpasa 
giresunspor|giresunspor
adanademirspor|adanademir mavisimsek
erzurumspor|erzurumspor
gaziantep|antepspor
karagumruk|karagumruk 
rizespor|rizespor
genclerbirligi|genclerbirligi

### Arama Komutu

Aşağıdaki komut ile `count.txt` içerisinde arama yapılmıştır

`cat count.txt | egrep 'galatasaray|cimbom|ultraslan|1905' | awk '{$1=$1;print}' | cut -d" " -f1 | awk '{s+=$1} END {print s}'`

### Eşleşen Parola Sayıları

**takim**|**parola sayısı**
:-----:|:-----:
galatasaray|150848
fenerbahce|140523
besiktas|85493
trabzonspor|40332
bursaspor|7199
eskisehir|6054
karsiyaka|2041
goztepe|1701
samsunspor|1588
ankaragucu|1308
sivasspor|1104
konyaspor|785
adanaspor|781
sakaryaspor|774
altay|765
kayserispor|701
kocaelispor|696
denizli|555
antalyaspor|417
malatyaspor|350
kasimpasa|324
giresunspor|213
adanademirspor|194
erzurumspor|163
gaziantep|140
karagumruk|109
rizespor|105
genclerbirligi|36
