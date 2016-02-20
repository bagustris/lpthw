# bismillah, terus belajar, tanpa memikirkan masa depan (don't have plan), 
# ex25.py: lebih banyak latihan, tapi kali ini beda

def bagi_kata(stuff):
    """ Fungsi ini akan membagi kata-kata untuk kita."""
    kata = stuff.split(' ')
    return kata

def sort_kata(kata):
    """Menyortir kata-kata..."""
    return sorted(kata)

def print_pertama_kata(kata):
    """Print kata pertama setelah memunculkannya."""
    kata = kata.pop(0)
    print kata

def print_terakhir_kata(kata):
    """ Print kata terakhir setelah memunculkannya."""
    kata = kata.pop(-1)
    print kata

def sort_kalimat(kalimat):
    """ Mengambil kalimat utuh dan mengembalikannya dalam kata-kata tersortir)."""
    kata = bagi_kata(kalimat)
    return sort_kata (kata)

def print_pertama_dan_terakhir(kalimat):
    """Print kata pertama dari terakhir dari kalimat."""
    kata = bagi_kata(kalimat)
    print_pertama_kata(kata)
    print_terakhir_kata(kata)

def print_pertama_dan_terakhir_sorted(kalimat):
    "Sortir kata kemudian print kata pertama dan terakhir."""
    kata = sort_kalimat(kalimat)
    print_pertama_kata(kata)
    print_terakhir_kata(kata)

