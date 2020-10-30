# -*- coding: utf-8 -*-

class ShoppingCalculator:

    def __init__(self, budget=0):
        self.__budget = budget
        self.__basket = []

    def add_budget(self, budget):
        self.__budget += budget


    def buy(self, product_name, category, unit_price, amount):
        product = {
            "category": category,
            "product_name": product_name,
            "unit_price": unit_price,
            "amount": amount
        }
        self.__basket.append(product)

    @property
    def total_spent(self):
        total = 0
        for product in self.__basket:
            total_price = product["unit_price"] * product["amount"]
            total += total_price
        return total

    @property
    def spent_by_category(self):
        spent_by_category = {}
        for item in self.__basket:
            total_price = item["unit_price"] * item["amount"]
            spent_by_category[item["category"]] = spent_by_category.get(item["category"], 0) + total_price

        sorted_tuple = sorted(spent_by_category.items(), key=lambda x: x[1], reverse=True)

        sorted_spent_by_category = {}

        for item in sorted_tuple:
            sorted_spent_by_category[item[0]] = item[1]

        return sorted_spent_by_category

    @property
    def remaining(self):
        return self.__budget - self.total_spent

    def is_under_budget(self):
        return self.remaining >= 0


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

    shopping1.buy("playstation 4", "elektronik", 3500, 1)

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
