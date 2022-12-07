#!/usr/bin/python

from translate import Translator
t = Translator(from_lang="es", to_lang="en")
t = t.translate("Hola como estas")
print(t)
