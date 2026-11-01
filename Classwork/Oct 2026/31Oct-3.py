list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even=[]
odd=[]
prime=[]

for i in list:
    if i!=0:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        print("Zero is neither even nor odd")
        
for i in list:
    if i!=0:
        if i%1==0 and i%i==0 and i!=1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                prime.append(i) 
                    
print("Even numbers are:",even)
print("Odd numbers are:",odd)
print("Prime numbers are:",prime)

