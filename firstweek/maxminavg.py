numbers = [-5,23,0,-9,12,99,105,-43]
max = numbers[0]
n = 8
i = 1

while i<n:
    if numbers[i] > max:
        max = numbers[i]
    i = i + 1

print(max)    
