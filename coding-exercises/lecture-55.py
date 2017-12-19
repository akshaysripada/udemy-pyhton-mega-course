filename = "fruits.txt"
file = open(filename, 'r')
text = file.read()
file.close()
print(text)
