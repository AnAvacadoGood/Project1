#-------------------------------------------------------------------------------------------------------------
#Programmed by: Miko Tonthat
#Date: 06/27/19
#Description: Calculates the cost of separate markers and marker packages together, including tax and shipping
#-------------------------------------------------------------------------------------------------------------

#input amount of markers wanted to buy
markers = int(input("How many markers are you buying? "))

#cost of separate markers and packages
markers_cost = .90
marker_packages_cost = 4.20

#divides amount of markers by amount in a package and gets the integers for the marker packages
marker_packages = markers//5
print("Number of packages:", marker_packages)

#divides amount of markers by amount in a package and gets the remainders for the separate marker
separate_markers = markers % 5
print("Number of separate markers:", separate_markers)

#calculates cost of marker packages and separate markers together
subtotal = (marker_packages_cost * marker_packages) + (markers_cost * separate_markers)
print("Subtotal:$", format(subtotal, '.2f'))

#calculates the tax before the total
tax = subtotal * 0.075
print("Tax:$", format(tax, '.2f'))

#calculates the shipping cost before the total and tax
shipping_cost = subtotal * 0.04
print("Shipping:$", format(shipping_cost, '.2f'))

#calculates the total by adding tax, shipping, and subtotal
total = subtotal + tax + shipping_cost
print("Total:$", format(total, '.2f'))
