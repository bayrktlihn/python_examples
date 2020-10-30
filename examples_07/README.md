# Q1 sezar sifreleme methodunu yazınız
```python
def sezar_sifrele(kaydirilacak_harf_sayisi, acik_metin):
    pass
```
[Örnek Kodu](q1.py)

https://tr.wikipedia.org/wiki/Sezar_%C5%9Fifrelemesi

# Q2 ShoppingCalculator sınıfını yazınız.
sınıfıniz, main() içinde yazılı olan kod ile uyumlu calismalidir.

```python
class ShoppingCalculator:
    # TODO: class ShoppingCalculator sınıfını yazınız.
    pass


def main():
    # surucu(driver) kodu:
    shopping1 = ShoppingCalculator(300)  # bütçe olarak 300 TL'miz var.
    shopping1.add_budget(100)  # 100 daha geldi.

    # ürün adı, kategori, birim fiyat, kaç tane
    shopping1.buy("domates", "gida", 20, 1)

    # ürün adı, kategori, birim fiyat, kaç tane.
    # aşağıda, birimden 2 tane almisiz, yani 15*2=30 TL harcama olacak.
    shopping1.buy("patates", "gida", 15, 2)

    shopping1.buy("deterjan", "temizlik", 20, 2)
    shopping1.buy("sabun", "temizlik", 40, 2)

    print(shopping1.is_under_budget())  # bütçe dahilinde miyiz?
    print(shopping1.total_spent)  # toplamda kaç TL harcadik?
    print(shopping1.remaining)  # toplamda kaç TL butcemiz kaldı?

    shopping1.buy("elektronik", "playstation 4", 3500, 1)

    print(shopping1.is_under_budget())  # bütçe dahilinde miyiz?
    print(shopping1.total_spent)  # toplamda kaç TL harcadik?
    print(shopping1.remaining)  # toplamda kaç TL butcemiz kaldı?

    # her kategori için kaç TL harcadigimizi bulalım.
    spent_by_category = shopping1.spent_by_category
    assert isinstance(spent_by_category, dict)
    # bu dict'in ilk elemani kategori adı (örneğin "gida"),
    # ikinci elemani da o kategori için toplamda kaç TL harcadik, o olacak.
    # dict'in ilk elemani, en yüksek harcama olsun, yani o kategorideki harcamaya göre
    # büyükten kucuge sıralı olsun.
   for category in spent_by_category:
        print(category, spent_by_category[category])


if __name__ == "__main__":
    main()

```

[Örnek Kodu](q2.py)

# Q3 tokenize()
bir string'i kelimelere ayiran, aşağıdaki fonksiyonu yazınız

```python
def tokenize(haystack: str, min_allowed_length=3):
    """
    Tokenizes a string.

    str1 = r"\tech\Python\ML, AI\Kaggle\Relationship_between_Earthquakes_and_Solar_System"
    tokens = tokenize(str1)
    print(tokens)

    ['tech', 'Python', 'ML', 'AI', 'Kaggle', 'Relationship', 'between', 'Earthquakes', 'and', 'Solar', 'System']

    :param min_allowed_length: only the words longer than this is accepted, others are ignored.
    :param haystack: string to tokenize
    :return: tokens as list of strings.
    """

```

[Örnek Kodu](q3.py)

# Q4 uniques_only()
```python
def uniques_only(iterable1):
    """
    Bir liste ya da tuple içindeki elemanlarin tekil olmayanlari atilmis halini donduren fonksiyon.
    işlem sonrasında, sıralama bozulmamalidir.
    [7, 6, 7, 2, 9, 2, 1] -> [7, 6, 2, 9, 1]
    """
    assert isinstance(iterable1, (list, tuple))
    # TODO: implement uniques_only(iterable1)
```

[Örnek Kodu](q4.py)

# Q5 q5 reverse_lookup()

```python
"""
Write a function named reverse_lookup that finds all of the keys in a dictionary that map to a specific value. The function will take the dictionary and the value to search for as its only parameters. It will return a (possibly empty) list of keys from the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise. Your program should create a dictionary and then show that the reverseLookup function works correctly when it returns multiple keys, a single key, and no keys. Ensure that your main program only runs when the file containing your solution to this exercise has not been imported into another program.
"""
```

[Örnek Kodu](q5.py)
