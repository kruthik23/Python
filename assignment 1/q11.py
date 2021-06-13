s = "SOFTWARE"

# with using slice operator

print(s[1:len(s):2]+s[0:len(s):2])
res_odd = ""
res_even = ""

# without using slice operator
for i in range(0, len(s)):
    if(i % 2 == 1):
        res_odd += s[i]
    else:
        res_even += s[i]
print(res_odd+res_even)