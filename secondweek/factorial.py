#Write a recursive function which calculates the factorial of a given number. 
# Use exception handling to raise an appropriate exception if the input parameter is not a 
# positive integer, but allow the user to enter floats as long as they are whole numbers.
import math
def factorial( n ):
   if n ==0:   # base case
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
 #      print(str(n) + '! = ' + str(returnNumber))
       return returnNumber
fact = factorial(5)
print(fact)


