# ex32.py

the_count = [1, 2, 3, 4, 5] 
fruit = [ 'apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop through a list
for number in the_count:
    print "This is count %d" % number
    
# same as above
for fruit in the_count:
    print "A fruit of type: %s" % fruit

# change    
for i in change:
    print "I got %r" % i
    
# build list
elements = []

# count  0-5
for i in range(0,6):
    print "Adding %d to the list." % i
    # append to the list
    elements.append(i)
    
# print
for i in elements:
    print "Element was: %d" % i
     
