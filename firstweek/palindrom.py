#s= input("word: ")
s="abba"
text = list(s)
print(text)
i=0
size = len(text)
ispalindrom=1

while i<(size/2):
    n=size-1-i
    if text[i]==text[n]:
        i=i+1
    else:
        ispalindrom=0
        break
        
if ispalindrom==1:
    print("a palindrom")
else:
    print("not a palindrom")