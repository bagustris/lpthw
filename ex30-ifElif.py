# ex30.py : if-elif-else

people = 30
cars = 40
trucks = 15

if cars > people:
    print "we should take cars"
elif cars < people:
    print "we should not take cars"
else:
    print "we can't decide"

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the truck"
else:
    print "we still can't decide"

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
