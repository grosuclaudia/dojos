def calculatorfunc(a,b,operatie="+", output_format="float"):
    if operatie is "+":
        if output_format is "float":
            return(float(a+b))
        else: return(int(a+b))

    if operatie is "-":
        if output_format is "float":
            return(float(a-b))
        else: return(int(a-b))
        

    if operatie is "*":
        if output_format is "float":
            return(float(a*b))
        else: return(int(a*b))

    if operatie is "/":
        if output_format is "float":
            return(float(a/b))
        else: return(int(a/b))  
      

print(calculatorfunc(2,3.0,"*","int"))
print(calculatorfunc(2,3.0))
