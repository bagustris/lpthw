def bagi_kata2(stuff):
    """ Fungsi ini akan membagi kata-kata untuk kita."""
    kata2 = stuff.split(' ')
    return kata2

def sortir_kata2(kata2):
    """Menyortir kata-kata..."""
    return sorted(kata2)

def print_pertama_kata(kata2):
    """Print kata pertama setelah memunculkannya."""
    kata = kata2.pop(0)
    print kata

def print_terakhir_kata(kata):
    """ Print kata terakhir setelah memunculkannya."""
    kata = kata2.pop(-1)
    print kata

def sortir_kalimat(kalimat):
    """ Mengambil kalimat utuh dan mengembalikannya dalam kata-kata tersortir)."""
    kata2 = bagi_kata2(kalimat)
    return sortir_kata2(kata)

def print_pertama_dan_terakhir(kalimat):
    """Print kata pertama dari terakhir dari kalimat."""
    kata = break_words(kalimat)
    print_pertama_kata(kata)
    print_terakhir_kata(kata)

def print_pertama_dan_terakhir_sorted(kalimat):
    """Sortir kata kemudian print kata pertama dan terakhir."""
    kata = sortir_kalimat(kalimat)
    print_pertama_kata(kata2)
    print_terakhir_kata(kata2)

