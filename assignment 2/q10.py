n = int(input("Enter limit : "))
a = []
for i in range(0, n):
    a.append(int(input("Enter : ")))
a.sort(reverse=True)
print(a)