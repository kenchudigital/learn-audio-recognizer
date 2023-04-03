import re

with open("test.ass", "r") as grilled_cheese:
    lines = grilled_cheese.readlines()

list_of_string = []

for words in lines:
    a = re.sub(r'Dialogue:.+}', "", words, count=0, flags=0)
    a = a.replace('\n', '')
    list_of_string.append(a)

file = open('items.txt','w')
for item in list_of_string:
    file.write(item+"\n")
file.close()