import math
def hypothenuse(a,b):
    try:
        return math.sqrt(a**2+b**2)
    except TypeError:
        return None
print(hypothenuse(12, 34))
print(hypothenuse("12", "34"))
print(hypothenuse(12, "34"))
