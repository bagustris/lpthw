# ex33.py: while-loops

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers no: ", numbers
    print "At bottom i is %d" % i
    
print "The numbers: "

for num in numbers:
    print num  
