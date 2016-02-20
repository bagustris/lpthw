cars = 100
space_in_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers	# misal: perusahaan taxi
cars_driven = drivers
carpool_capacity = cars_not_driven - space_in_car
average_pasengers_per_car = passenger / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passenger, "to carpool today."
print "we need to put about", average_pasengers_per_car, "in each car"
