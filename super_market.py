prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

total = 0

for key in prices:

  print key.upper()
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  each_total = 0;
  each_total = each_total + (prices[key] * stock[key])
  total = total + each_total
  print "total: %s" % each_total
  print

print "TOTAL: %s" % total
