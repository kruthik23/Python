N = int(input("Enter N : "))
if(N >= 0 and (1 <= N and N <= 20)):
    for i in range(1, N):
        if(i < N):
            print(i**2)
else:
    print("N is non-negative integer not allowed!")