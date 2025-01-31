# lumpsum calculator
Lumpsum=float(input("Enter the sum : "))
Expreturn=float(input("Enter the expected return : "))
Year=int(input("Enter no of years : "))
x=float(Lumpsum+(Lumpsum*(Expreturn/100)))
for y in range(Year-1):
    x=x+(x*(Expreturn/100))
print(f"The total Amount will be {round(x)} for {Year} years with {Expreturn} % of return per year")