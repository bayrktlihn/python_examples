# Q1 middlestrip()
Bir string alıp, içindeki boşlukları silen bir fonksiyon yazınız.
Bu işlem sonrasında, parametrenin solundaki ve sağındaki boşluklar kalıyor olmalıdır.

"   aa b c   "
"   aabc   "

```python
def middlestrip(string1):
    pass
```


[Örnek Kodu](quest_01.py)

# Q2 stars
```python
def print_stars(num):
    pass
```

1 için:
*

2 için:
*
**

3 için:
*
**
***


[Örnek Kodu](quest_02.py)

# Q3
```python
def alti_cizili_yaz(baslik, karakter):
    print(baslik)
    print(len(baslik) * karakter)
```


ahmet
_____


[Örnek Kodu](quest_03.py)

# Q4
Bir sayıya kadar olan sayıların toplamını döndüren bir fonksiyon yazınız.
```python
def sum_up_to(number):
    pass
```

sum = n(n+1)/2


[Örnek Kodu](quest_04.py)

# Q5
verilen bir sayıya kadar olan asal sayıları bulan uygulama. 

yukarıdaki is_prime() fonksiyonu kullanabilirsiniz.


[Örnek Kodu](quest_05.py)

# Q6
verilen bir sayidan büyük bir sonraki asal sayiyi bulan uygulama.

[Örnek Kodu](quest_06.py)

# Q7 zaman hesaplama
* t = x/v formülünü kullanalım.
* iki parametre döndürsün: saat ve dakika

```python
def zaman_hesapla(ortalama_hiz, mesafe):
    """
    Ortalama hiz ve mesafe kullanarak sureyi hesaplar.

    bu fonksiyon soyle cagirilir:
    saat, dakika = zaman_hesapla(ortalama_hiz, mesafe)

    :param ortalama_hiz:
    :param mesafe:
    :return:
    """
    pass
```


[Örnek Kodu](quest_07.py)

# Q8 shout()
* shout isimli bir fonksiyon yazınız.
* Bu fonksiyon:
    * string tipinden bir parametre almalıdır.
    * her karakteri büyük harfe çevirmelıdır.
    * her karakterin arasina bir boşluk koymalıdır.
    * sonuna da ünlem eklemelidir.

Uygulama: shout()
```python
def shout(needle):
    """
    strip()
    hersey uppercase
    her bir karakter arasina bir " " koysun.
    sonunda da unlem yoksa eklesin.

    "no i will not": "N O  I  W I L L  N O T !"
    :type needle: str
    :param needle:
    :return:
    """
```
    

[Örnek Kodu](quest_08.py)
    
# Q9
whisper()

shout() fonksiyonunun tersi.

hepsini küçük harfe cevirecek, aradaki fazla bosluklari atacak, sonda unlem varsa kaldiracak.


[Örnek Kodu](quest_09.py)
