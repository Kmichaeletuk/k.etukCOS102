print("1. Compound Interest 2. Simple interest 3. Anuity plan ")
Sel =int(input("select the number"))
if Sel == 1:
    p=int(input("enter the initial principal:"))
    r=int(input("enter the rate percentage: "))
    t=int(input("enter the time period:"))
    n=int(input("enter the no of times to calculate interest:"))
    a=p*((1+r/n) ** (n*t))
    print(a)
elif Sel == 2:
    p=int (input ("Enter pricipal : "))
    t=int (input ("Enter time : ") )
    r=int (input ("Enter rate : "))
    si=(p*t*r) /100
    print ("Simple Interest is : ", si)
elif Sel == 3:
    p = float(input("Enter principal: "))
    r = float(input("Enter annual interest rate (as a decimal): "))
    t = int(input("Enter time (in years): "))
    annuity = p * (1 - (1 + r) ** (-t)) / r

    print("Annuity amount is:", annuity)
