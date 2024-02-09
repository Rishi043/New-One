import math
p=float(input("Enter Principal Amount:"))
r=float(input("Enter Annual Rate of Interest:"))
t=int(input("Enter Time(in Yrs):"))
print("1.Calculate Simple Interest")
print("2.Calculate Compound Interest")
print("3.Calculate Both SI and CI")
choice=int(input("Enter your choice(1 or 2 or 3):"))
print("-"*88)
print ("\t\t\t\tR.E.S.U.L.T.S")
if (choice==1) :   #calculate simple interest
    si=(p*r*t)/100
    print("Simple Interest:"+str(round(si,2)))
    print("Amount after interest:"+str(round(p+si,2)))
elif (choice==2):  #calculate compound interest
    r=r/100
    a=p*pow((1+r),t)
    ci=a-p
    print("Compound Interest:"+str(round(ci,2)))
    print("Amount after interest:"+str(round(a,2)))
    
else:    #calculating Both
    si=(p*r*t)/100
    print("Simple Interest:"+str(round(si,2)))
    print("Amount after interest:"+str(round(p+si,2)))
    print("-"*88)
    r=r/100
    a=p*pow((1+r),t)
    ci=a-p
    print("Compound Interest:"+str(round(ci,2)))
    print("Amount after interest:"+str(round(a,2)))
print("-"*88)
print("\t\t\t\tT.H.A.N.K  Y.O.U")
