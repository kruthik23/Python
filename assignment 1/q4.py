my_str = input("Enter string  : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed String is: ", str)

print("Reverse of the string: "+my_str[::-1])