r = int(input("Enter the number of rows: "))  
for i in range(r + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  

# Add checks for value of n - can it be string? can it be -100?
