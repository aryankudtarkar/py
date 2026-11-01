while True:
    print("Factorial Values")
    x=int(input("Enter a number: "))
    i=1
    while i<=x:
        fact=1
        j=1
        while j<=i:
            fact=fact*j
            j+=1
        print("Factorial of",i,"is",fact)
        i+=1
    z=int(input("Wanna try again? (1 for Yes, 0 for No): "))
    if z!=1:
        break 
