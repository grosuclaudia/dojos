#this function adds two numbers
def add (x,y):
    return x+y
    #this function substracts two numbers
    def substract (x,y):
        return x-y
        #this function multiply two numbers 
        def multiply(x,y):
            return x*y
            #this function divides two numbers
            def divide (x,y):
                return x/y  
x=input('Enter a number:')
z=input('Enter an operation:')
y=input('Enter a second number:')
if z==add:
    print(x+y)
    