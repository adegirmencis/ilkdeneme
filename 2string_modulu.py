#!/usr/bin/python
#-*- coding: utf-8 -*-

# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)

# küçük bir uygulama
# kendi türkçe karakter destekli lovercase fonksiyonumuzu yazınız.?

def kucukHarfler():
    import string
    harfler = string.ascii_lowercase+"çğşıöü"
    def ayikla(param):
        if param not in 'xwq':
            return True
        return False
    harfler = list(filter(ayikla,harfler))
    harfler = "".join(harfler)
    return harfler

print(kucukHarfler())