#Programmed by: Miko Tonthat
#Date: 07/03/19
#Description: This program determines your total wage depending on the time you've worked.

#function calculates total wage depending on time(considers overtime)
def wages(worked, rate):
    if worked <= 40:
        return (rate * worked)
    else:
        return (rate * 40) + ((worked - 40) * rate * 1.5)

#main program
def main():
    #input
    worked = float(input("Numbers of hours worked: "))
    rate = float(input("Hourly rate: "))
    #output/results
    total_wage = wages(worked, rate)
    print("Total wages: $", format((total_wage), '.2f'))
    
main()