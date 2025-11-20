# Training set OG:
import random


list_of_list = []
inList = []

for i in range(100):
    inList = []
    for i in range(3):
        random_int = random.randint(1,1001)
        inList.append(random_int)
    list_of_list.append(inList)

print(list_of_list)