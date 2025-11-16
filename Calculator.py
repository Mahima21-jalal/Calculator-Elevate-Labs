print("Welcome to Mahima's Calculator.... ")
while (True):
    expression=input("Enter mathamatical operator \n : E exit\n")
    if expression=="E" or expression== "e":
        print("Are you sure y/n")
        
        check_assurace=input().upper()
        if check_assurace=="Y":
            break
        else:
            continue
        
    elif expression== "+" or expression== "-" or expression== "*" or expression== "/" or expression=="**" or expression=="%":
        pass
    else:
        print("Sorry ! You entered invalid operator") 
        continue
    x=(input("Enter value of x : "))
    y=(input("Enter value of y : "))
    
    if x.isnumeric() and y.isnumeric():
        pass
    else: 
        print("You can enter only numeric values")
        continue
    x=float(x)  
    y=float(y)
    if expression=="+":
        print(x+y)    
    elif expression== "-":
        print(x-y)
    
    elif expression== "*":
        print(x*y)
    
    elif expression=="/":
        print(x/y)

    elif expression=="**":
        print(x**y)

else:
        print("Invalid oprator")
    

    
    

