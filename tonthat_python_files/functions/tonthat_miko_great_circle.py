#Programmed by: Miko Tonthat
#Date: 07/01/19
#Description: This program calculates the distance between 2 cities using latitude and longitude.

#math module
import math

#function for calculating the kilometers and converting degrees to radians
def great_circle_distance(lat1, long1, lat2, long2):
    radius = 6371
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    θ = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(math.fabs(long1 - long2)))
    d = radius * θ
    return d

#function for converting kilometers to miles
def km_to_miles(distance):
    km_mile = 0.621371
    result = distance * km_mile
    return result


def main():
    #variables
    SJ_lat = 37.33
    SJ_long = -121.9
    CHI_lat = 41.83
    CHI_long = -87.68
    DC_lat = 38.90
    DC_long = -77.02
    sj_to_chi = great_circle_distance(SJ_lat, SJ_long, CHI_lat, CHI_long)
    ch_to_dc = great_circle_distance(CHI_lat, CHI_long, DC_lat, DC_long)
    #results
    print("Distance from San Jose to Chicago is", int(sj_to_chi), "km or", int(km_to_miles(sj_to_chi)), "miles.") 
    print("Distance from San Jose to Chicago is", int(ch_to_dc), "km or", int(km_to_miles(ch_to_dc)), "miles.")

main()