from collections import Counter
Astr = "How do you do"
char = 'o'
# Given String and Character
print("Given String:\n", Astr)
print("Given Character:\n",char)
count = Counter(Astr)
print("Number of time character is present in string:\n",count['o'])