#  Star Pyramid
for i in range(5):  # i traverse 0 to 4
    for j in range(5,i,-1):  # reverse traverse loop and print space j times 
        print(" ",end=" ")
    for k in range((2*i)+1):  # k traverse 0 to 2*i and print * k times
        print("*",end=" ")
    print()