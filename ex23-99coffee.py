#!/usr/bin/env python

"""
99 botol kopi di dinding
dibuat simple dengan python
lebih simple lagi dengan bahasa Indonesia
"""

for jumlah in range (99, 0, -1): #
    if jumlah > 1:
        print (jumlah, "jumlah botol kopi di dinding, ", jumlah, "botol kopi.")
        if jumlah > 2:
            suffix = str (jumlah - 1) + " botol kopi di dinding."
        else:
            suffix = " 1 botol kopi di dinding."
    elif jumlah == 1:
        print "1 botol kopi di dinding, 1 botol kopi."
        suffix = "Tidak ada kopi lagi di dinding."
    print "Ambil satu, lewatkan, ", suffix
    print "__"
