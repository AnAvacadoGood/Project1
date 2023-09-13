#---------------------------
#Programmed by: Miko Tonthat
#Date:06/19/19
#---------------------------

degrees_celsius = float(input("Enter temperature in degrees Celsius:"))
wind_velocity = float(input("Enter wind velocity in kilometers/hour:"))

Temperature = degrees_celsius
Velocity = wind_velocity

wind_chill_temperature = 13.12 + (0.6215 * Temperature) - (11.37 * Velocity ** 0.16) + (0.3965 * Temperature * Velocity ** 0.16)
print("The wind chill temperature in degrees Celsius is", format(wind_chill_temperature, '.3f'))