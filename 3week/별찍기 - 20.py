count = int(input())
oddEven = 0
for i in range(count):
    count -= i
    if count == 1:
        print("*", end="")
    else:
        print("*", end=" ")
    oddEven = 1
    for j in range(i)