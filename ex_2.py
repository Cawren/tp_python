def mediane(a, b, c) :
    if (a > b and a < c) or (a < b and a > c) :
        return a
    elif (b > a and b < c) or (b < a and b > c) :
        return b
    else :
        return c
    
a = input("Input the first number : ")
b = input("Input the second number : ")
c = input("Input the third number : ")
print(f"Median of the above three numbers -\n{mediane(a,b,c)}")