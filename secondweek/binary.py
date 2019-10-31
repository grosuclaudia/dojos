number,base = input("Enter two values: " ). split()
allowed=["2","10"]
if base  not in allowed:
    print("You are not allowed: ")
print(number,base)


def binary_function(binary):
    decimal = 0
    binary=base
        # length of binary input
    l = len(binary)

    # loop through each digit of binary
    for x in binary:
        l = l - 1  # decrease l by 1
        decimal += pow(2, l) * int(x)  # multiply
    return("Decimal of {p} is {q} ".format(p=binary, q=decimal))






def decimal_function(n):
    x = n
    k = []
    while n != 0:
        a = (n % 2)
        k.append(a)
        n = n // 2
    # k.append(0)
    string = ""
    for j in k[::-1]:
        string = string + str(j)
    return ('The binary no. for %d is %s' % (x, string))


if base == "2":
    print(binary_function(number))
else:
    print(decimal_function(int(number)))
