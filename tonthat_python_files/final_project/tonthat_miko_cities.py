#Programmed by Miko Tonthat
#Date: 07/24/19
#Description: This program works with cities and returns them with the country it belongs to and the population.

#used to capitalize each word
def capitalize_city(city):
    city = city.title()
    return city

#calculates the average population of all the cities
def average(population, n_cities):
    average = population / n_cities
    return int(average)

#main program
def main():
    #opens file
    in_file = open('cities.txt', 'r')
    my_dictionary = {}
    total = 0
    #strips/splits each line and creates a dictionary with the city as the key and the country and population as the value
    for line in in_file:
        info = line.strip().split(',')
        city = info[0]
        country = info[1]
        population = int(info[2])
        my_dictionary[city] = [country, population]
        total = total + population
    #closes file
    in_file.close()
    n_cities = len(my_dictionary.keys())
    #output amount of cities + average population of them
    print("Number of cities:", n_cities)
    print("Average population:", format(average(total, n_cities), ',d'))
    #for spacing
    print()
    #validates input
    need_input = True
    while need_input:
        wanted_city = input("Enter a city, or just Enter to quit:")
        capitalized = capitalize_city(wanted_city)
        if wanted_city != '':
            pass
            #gets the city and outputs the country and population corresponding to the city
            if capitalized in my_dictionary.keys():   
                wanted = my_dictionary[capitalized]
                print(capitalized, "is in", wanted[0], "and has a population of", format(wanted[1], ',d') + '.')
            else:
                #prints error when the key is not within the dictionary
                print(capitalized, "is not in the list, sorry.")
            #spacing
            print()       
        else:
            need_input = False
    
main()

