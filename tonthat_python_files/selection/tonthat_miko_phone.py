#Programmed by: Miko Tonthat
#Date: 07/03/19
#Description: This program decides whether phone service 1 or 2 is cheaper by calculating the base cost and the cost when over the limit. 

#function for units
def get_units():
    units = int(input("Enter number of units used: "))
    return units

#function to calculate the cost of plan 1 and 2
def calculate_cost(units, base_cost, base_limit, cost_over):
    if units <= base_limit:
        result = base_cost
    else:
        result = base_cost + (cost_over * (units - base_limit))
    return result

#main program    
def main():
    #costs and units
    units = get_units()
    if (units >= 0):
        phone_service1 = 9.38
        service_over1 = 65
        service_over_cost1 = .045
        phone_service2 = 8.57
        service_over2 = 50
        service_over_cost2 = .052
        #output/results 
        cost1 = calculate_cost(units, phone_service1, service_over1, service_over_cost1)
        cost2 = calculate_cost(units, phone_service2, service_over2, service_over_cost2)
        print("Cost for plan 1: $", format(cost1, '.2f'))
        print("Cost for plan 2: $", format(cost2, '.2f'))
        if cost1 < cost2:
            print("Plan 1 is cheaper.")
        else:
            print("Plan 2 is cheaper.")
    else:
        print("You cannot have negative units.")
        
main()