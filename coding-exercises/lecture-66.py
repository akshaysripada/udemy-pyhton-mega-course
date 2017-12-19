def write_to_file(temperatures, filename):
    file = open(filename, 'w')
    for c in temperatures:
        if c > -273.15:
            f = c * (9/5) + 32
            file.write(str(f) + '\n')
    file.close()

temperatures=[10,-20,-289,100]
filename = "temperature.txt"
write_to_file(temperatures, filename)

file = open(filename, 'r')
print(file.read())
file.close()
