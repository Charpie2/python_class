

# input

PV = float(input("Enter the starting principle: "))
R = float(input("Enter the annual interest rate: "))
T = float(input("For how many years will the account earn interest?: "))
M = float(input("How many times per year is the intertest compounded?: "))

# compute 

FV = PV * (1 + (R/100) / M)**(M*T)

# output

print("At the end of the year you will have: $", end = '')
print(round(FV, 2))