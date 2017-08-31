def hotel_cost(nights):
  if type(nights) == int:
    return 140 * nights
  else:
    return "Error"

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return "City does not have a flight"

def rental_car_cost(days):
  total_cost = days * 40
  if days >= 7:
    return total_cost - 50
  elif days >= 3:
    return total_cost - 20
  else:
    return total_cost

def trip_cost(city, days, spending_money):
  return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print "Hotel Cost"
print "Hotel Cost for 4 days is %r" % hotel_cost(4)
print "Hotel Cost for 4.0 days is %r" %hotel_cost(4.0)
print "Hotel Cost for 'a' days is %r" %hotel_cost('a')

print "Plane Ride Cost"
print "Plane Ride Cost for Charlotte is %r" % plane_ride_cost("Charlotte")
print "Plane Ride Cost for Tampa is %r" % plane_ride_cost("Tampa")
print "Plane Ride Cost for Pitt is %r" % plane_ride_cost("Pittsburgh")
print "Plane Ride Cost for LA is %r" % plane_ride_cost("Los Angeles")
print "Plane Ride Cost for SLO is %r" % plane_ride_cost("San Luis Obispo")

print "Rental Car Cost"
print "Rental Car Cost for 2 days is %r" % rental_car_cost(2)
print "Rental Car Cost for 3 days is %r" % rental_car_cost(3)
print "Rental Car Cost for 4 days is %r" % rental_car_cost(4)
print "Rental Car Cost for 7 days is %r" % rental_car_cost(7)
print "Rental Car Cost for 10 days is %r" % rental_car_cost(10)

print "Total Trip Cost"
print "Total Trip Cost to Tampa for 4 days with 400 spending is %r" % trip_cost("Tampa", 4, 400)
