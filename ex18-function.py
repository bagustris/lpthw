# ex18.py : name, variables, function
# usage :

# perintah ini seperti scrip sebelumnya dengan argv
def print_dua(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args diatas pointless, kita dapat lakukan sbb
def print_dua_lagi(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# perintah berikut menggunakan 1 argumen
def print_satu(arg1):
  print "arg1: %r" % arg1

# perintah berikut tidak menggunakan argumen
def print_tidakada():
  print "Saya tidak mendapatkan apa-apa"

print_dua("Bagus", "Tris")
print_dua_lagi("Bagus","Tris")
print_satu("Pertama")
print_tidakada()
