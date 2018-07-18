# ex20.py fungsi dan file
# usage : python ex20.py input_file

from sys import argv

script, input_file = argv  # untuk memanggil input_file? 
  
def print_semua(f):     # mendefinisikan fungsi print_semua
    print f.read()      # membaca fungsix 

def rewind(f):
    f.seek(0)           # membaca posisi

def print_baris(baris_ke, f):
    print baris_ke, f.readline() # membaca baris

file_sekarang = open(input_file) # membuka file

print "Ayo kita print keseluruhan file:\n"
print_semua(file_sekarang)

print "Sekarang ayo kita putar ulang, seperti tape"
rewind(file_sekarang)

print "Ayo kita print tiga baris saja:"
baris_sekarang = 1
print_baris(baris_sekarang, file_sekarang)

baris_sekarang = baris_sekarang + 1
print_baris(baris_sekarang, file_sekarang)

baris_sekarang = baris_sekarang + 1
print_baris(baris_sekarang, file_sekarang)


