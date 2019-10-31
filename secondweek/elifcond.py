temperature=float(input())
if temperature < 0:
    print("Below freezing")
elif temperature < 10:
    print("Very cold")
elif temperature < 20:
    print("Chilly")
elif temperature < 30:
    print("Warm")
elif temperature < 40:
    print("Hot")
else:
    print("Too hot")