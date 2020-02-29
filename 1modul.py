#!/usr/bin/python
#-*- coding: utf-8 -*-
# # # uygulama
# harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# sayilar=[1,2,3,4,5,6,7,8,9,0]
# # # yukarıdaki listeden rastgele iki karakterli bir şifre üretin
# import random
# harf_key = random.randint(0,25)
# sayi_key = random.randint(0,9)
# sifre = str(harfler[harf_key])+str(sayilar[sayi_key])
# print(sifre)
#
# # aynı örneği choice ile çözelim
# sifre = random.choice(harfler)+str(random.choice(sayilar))
# print(sifre)

# harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# sayilar=[1,2,3,4,5,6,7,8,9,0]
# # kullanıcıdan alınan karakter adedince şifre üreten uygulamayı
# # kaç karakterli şifre istersiniz (3-10 arası bir sayı gir)

harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sayilar=[1,2,3,4,5,6,7,8,9,0]
import random
hane = int(input("Kaç karakterli şifre oluşturmak istediğinizi giriniz.\n Minimum 3, maksimum 10 karakter olabilmektedir."))
karakterler = harfler + sayilar
# print(karakterler)
sifre_pH = random.choices(karakterler, k = hane)
# print(sifre_pH)
sifre_pH= map(lambda x: str(x),sifre_pH)
sifre = "".join(sifre_pH)
print(sifre)

