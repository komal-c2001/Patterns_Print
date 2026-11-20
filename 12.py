# Butterfly Pattern 
for i in range(5):
    for j in range(i+1): 
        print("*",end=" ") # print * j times
    for j in range(4,i,-1):  # reverse traverse loop and print space j times 
            print(" ",end=" ")
    for j in range(4,i,-1):  # reverse traverse loop and print space j times 
            print(" ",end=" ")
    for k in range(i+1):  # k traverse 0 to i and print * k times
        print("* ",end="")
    print()
for i in range(5):
    for j in range(4,i,-1): 
        print("*",end=" ") # print * j times
    for j in range(i+1):  # j traverse 0 to i  and print space j times 
            print(" ",end=" ")
    for j in range(i+1):  # j traverse 0 to i  and print space j times 
            print(" ",end=" ")
    for k in range(4,i,-1):  # k traverse 4 to i and print * k times
        print("* ",end="")
    print()