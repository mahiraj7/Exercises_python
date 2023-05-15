n = int(input("Enter the number of rows"))  
for i in range(0, n):  
    for j in range(0, i + 1): 
        print("* ", end="")       
    print()  

# Add checks for value of n - can it be string? can it be -100?
