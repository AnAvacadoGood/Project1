#Programmed by Miko Tonthat
#Date: 07/15/19
#Description: This program reads the list of densities of different planets and sorts them to find out the minimum, maximum, average, and median density.

#used to find the average of the densities
def average(mylist):
    average = sum(mylist) / len(mylist)
    return average
#makes a copy of the original file and finds the value in the center of the list after sorting
def median(mylist):
    copy = mylist[:]
    copy.sort()
    number = len(copy)
    if number % 2 != 0:
        median = copy[(number - 1) // 2]
    else:
        median = (copy[(number // 2)] + copy[(number // 2) - 1]) / 2.0
    return median

#main program
def main():
    #opens file
    in_file = open('density.txt', 'r')
    mylist = []
    #gets rid of \n and splits line into separate elements of a list
    for line in in_file:
        line = line.strip()
        info = line.split()
        planet = info[0]
        density = float(info[1])
        print(planet, density)
        mylist.append(density)
    #closes file
    in_file.close()
    #output    
    print("The minimum density is", format(min(mylist), '.2f'))
    print("The maximum density is", format(max(mylist), '.2f'))
    print("The average density is", format(average(mylist), '.2f'))
    print("The median density is", format(median(mylist), '.2f'))
    
main()