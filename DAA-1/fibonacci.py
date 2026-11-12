def rec_fun(n): 
    if n < 0: 
        print("Invalid input") 
        return 
    a, b = 0, 1 
    for i in range(n): 
        print(a, end=" ") 
        a, b = b, a + b

def rec(n):
    if n <=1:
        return n 
    return(rec(n-1) + rec(n-2))

if __name__ == '__main__':
    n = int(input("Enter the limit: "))

    print("Without recusrion: ", end=" ")
    rec_fun(n)

    print("")

    print("With recusrion: ", end=" ")

    for i in range(n):
        print(rec(i),end=' ')