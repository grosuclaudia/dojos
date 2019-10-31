#Fibonacci series:
#the sum of two elemnets defines next
a1,a2 = 0, 1
temp = 0
position=1
print(str(position) +". "+ str(a1))
position=position + 1 
a1= a1+a2
print(str(position) + ". "+str(a1))
position=position+1
print(str(position) + ". "+str(a1))



while position<30:
    position=position+1
    temp=a1
    a1=a2
    a2=a2+temp
    print(str(position) + ". "+str(a2))
