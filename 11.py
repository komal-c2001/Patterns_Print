# Hollow Right-Angled Triangle
for i in range(5):
    for j in range(i+1): 
        if j == 0 or i == j or i == 4:  # check i and j equal to 0 or 4 or i == j
            print("*",end=" ") # print * j times
        else:
            print(" ",end=" ")
    print()