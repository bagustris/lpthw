# ex5-varPrint.py: More variables and Printing

my_name = 'bagustris'
my_age = 26 # at current time
my_height = 160 # cm
my_weight = 50 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name		# string data, percent %
print "He's %d cm tall." % my_height		#
print "He is %d kg heavy." % my_weight
print "Actually that's not heavy."
print "He is got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print " I add %d,%d, and %d I get %d." % (my_age, my_height, my_weight, total)
