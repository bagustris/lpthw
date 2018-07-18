# ex20.py ; function can return something, the use of =

def add(a,b):
    print "Menambahkan %d + %d" % (a, b)
    return a + b

def subtract (a, b):
    print "Menguraning %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Mengalikan %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "Membagi %d / %d" % (a, b)
    return a / b

print "Ayo kita lakukan operasi matematik dengan beberapa fungsi"

age = add (30,5)
height = subtract (78,4)
weight = multiply (90,2)
iq=divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

what = add (age, subtract(height, multiply(weight,divide(iq,2))))

print "Itu akan menjadi: " ,what, "Dapatkah kamu mengerjakannya dengan tangan?"
