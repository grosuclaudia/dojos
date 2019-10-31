#print the top 25 three-digit natural numbers divisible by 7 or by 9.
#  Each number should be displayed in a separate line.
i=0
n=100
while i<25:
    if n%7==0 or n%9==0:                   
        i=i+1
        print (str(i)+"."+ str(n)) 
    n=n+1
    