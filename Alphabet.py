try:
    n = int(input("Enter the number of rows: "))  
    k = 0 
    for i in range (0,n):
        for j in range(0,i+1):
            char = chr(65 + k)
            k += 1
            k = k % 26
            print(char,end="")
        print()
except ValueError:
    print("That's not an int!")