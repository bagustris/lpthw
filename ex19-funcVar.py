def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party"
    print "Get a blanket.\n"

print "Kita dapat memberi nilai fungsi secara langsung:"
cheese_and_crackers(20, 30)

print "Atau, kita bisa menggunakan dua variabel untuk script:"
jumlah_cheese=10
jumlah_crackers=50

cheese_and_crackers(jumlah_cheese, jumlah_crackers)

print "Kita dapat melakukan operasi matematik juga:"
cheese_and_crackers(10+20, 5+6)

print "Dan kita dapat mengkombinasikan keduanya, variabel dan mat:"
cheese_and_crackers(jumlah_cheese +100, jumlah_crackers + 10000)

