# Hollow Square
for i in range(5):
    for j in range(5):
        if(i == 0 or i == 4 or j == 0 or j == 4): # check i and j equal to 0 or 4
            print("*",end=" ") # print * j times
        else:
            print(" ",end=" ")
    print()