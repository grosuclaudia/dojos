import random

at_lost = 0
def_lost = 0

x1 = random.randint(1,6)
x2 = random.randint(1,6)
x3 = random.randint(1,6)
attList = []
attList.append(x1)
attList.append(x2)
attList.append(x3)

y1 = random.randint(1,6)
y2 = random.randint(1,6)
defList = []
defList.append(y1)
defList.append(y2)

attList.sort(reverse=True)
defList.sort(reverse=True)

if (attList[0] > defList[0]):
    def_lost = def_lost + 1
else:
    at_lost = at_lost + 1

if (attList[1] > defList[1]):
    def_lost = def_lost + 1
else:
    at_lost = at_lost + 1

print(attList)
print(defList)

print("Dice:")
print(" Attacher: " + str(attList[0])+"-"+str(attList[1])+"-"+str(attList[2]))
print(" Defender: " + str(defList[0])+"-"+str(defList[1]))

print("Outcome:")
print(" Attackers: Lost " + str(at_lost) + " units")
print(" Defenders: Lost " + str(def_lost) + " units")

