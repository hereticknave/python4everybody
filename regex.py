import re
fh = open("regex_sum_303621.txt")
print(sum([int(i) for i in re.findall('[0-9]+',fh.read())]))
#y=sum(test_list)
#print(y)

