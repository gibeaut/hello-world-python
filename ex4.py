#Number of Cars
cars = 100
#Space in each car
space_in_a_car = 4.0
#Number of Drivers we have available
drivers = 30
#Number of passengers that want a ride
passengers = 90
#Number of cars we have without drivers
cars_not_driven = cars - drivers
#Number of cars we can drive
cars_driven = drivers
#How many people we can take
carpool_capacity = cars_driven * space_in_a_car
#Average number of people per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
