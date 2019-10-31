#idea bank
idea = input("What is your new idea: ")
nr = 0

file=open("ideabank.txt","a")
file.write(idea + "\n")
file.close()

file=open("ideabank.txt","r")
print("Your ideabank:")
for line in file:
    nr = nr + 1
    print(str(nr) + ". " + line)

file.close()