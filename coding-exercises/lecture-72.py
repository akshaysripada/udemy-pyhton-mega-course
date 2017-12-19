from datetime import datetime

filenames = ["file1.txt", "file2.txt", "file3.txt"]
save_filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")

with open(save_filename, 'w') as output_file:
    for f in filenames:
        with open(f, 'r') as input_file:
            output_file.write(input_file.read() + '\n')

output_file.close()
file = open(save_filename, 'r')
print(file.read())
file.close()
