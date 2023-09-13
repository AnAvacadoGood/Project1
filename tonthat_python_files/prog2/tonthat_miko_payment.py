#----------------------------
#Programmed by: Miko Tonthat
#Date: 6/19/19
#----------------------------

loan = float(input("Enter amount of loan:$"))
annual_interest_rate = float(input("Enter annual interest rate as a percent:"))
years_for_loan = int(input("Enter number of years for the loan:"))

monthly_rate = (annual_interest_rate / 12) / 100
months = years_for_loan * 12

payment = loan * (monthly_rate * (1 + monthly_rate) ** months) / ((1+monthly_rate)**months - 1)
print("Your monthly payment is $", format(payment, '.2f'))