#Programmed by: Miko Tonthat
#Date: 07/01/19
#Description: This program calculates the distance between two points using 2 different formulas to get 2 different results.

#math module
import math

#function to calculate pythagorean distance
def distance(x1, y1, x2, y2):
    result = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    return result

#function to calculate the city block distance
def block_distance(x1, y1, x2, y2):
    result = math.fabs((x1 - x2)) + math.fabs((y1-y2))
    return result


def main():
    #input the coordinates
    x1 = float(input("Enter first x: "))
    y1 = float(input("Enter first y: "))
    x2 = float(input("Enter first second x: "))
    y2 = float(input("Enter first second y: "))
    #results
    print("The Pythagorean distance is", format(distance(x1, y1, x2, y2), '.2f'))
    print("The city block distnace is", format(block_distance(x1,y1,x2,y2),'.2f'))
    
main()