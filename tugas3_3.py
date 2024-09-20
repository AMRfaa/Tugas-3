baris= 6
for i in range(baris):
    for j in range(baris- i - 1):
        print(" " * 2, end="")
    for j in range(i + 1):
        if j > 0:
            print(", ", end="")
        print("*", end=" ")
    print()
