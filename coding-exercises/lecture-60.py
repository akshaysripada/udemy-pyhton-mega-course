numbers = [1, 2, 3]

file = open("lec-60.txt" ,'w')

for i in numbers:
    file.write(str(i)+'\n')

file.close()

file = open("lec-60.txt" ,'r')
text = file.readlines()
print(text)
for i in text:
    print(i)
