filename = "fruits.txt"
file = open(filename, 'r')
text = file.readlines()
file.close()

print(text)

for line in text:
    # we subtract 1 since there is a newline char (\n) at the end of each line
    print(len(line) - 1)
