count = 0
while (count < 7):
    #print("The count is: {}".format(count)) #first way to print
    print(f"The count is", count) #second way to print
    count += 1


for a in range(0, 10):
    for b in range(0, 10 - a):
        print("&", end="")
    print()

for c in range(0, 10):
    for d in range(0, 1 + c):
        print("&", end="")
    print()
