"""
price_str = input("apple:")
weight_str = input("weight:")
price = float(price_str)
weight = float(weight_str)
total = price * weight
print (total)
#简化版本
price = float(input("apple:"))
weight = float(input("weight:"))
total = price * weight
print (total)
"""
apple = float(input("apple:"))
weight = float(input("weight:"))
total = apple * weight
print ("apple %.02f $/KG, weight %.02f kg, total %.02f" % (apple, weight, total))

scale = 0.25
print("data scale is %.2f%%" % (scale * 100))
