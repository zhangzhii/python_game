import struct

file = open("binary.dat", "wb")
for n in range(1000):
    data = struct.pack("i", n)
    file.write(data)
file.close()

file = open("binary.dat", "rb")
size = struct.calcsize("i")

bytes_read = file.read(size)
while bytes_read:
    value = struct.unpack("i", bytes_read)
    value = value[0]
    print(value, end=" ")
    bytes_read= file.read(size)
file.close()



#
# file = open("data2.txt", "w")
# file.write("Sample file writing\n")
#
# text_lines = [
#     "chapter3\n",
#     "sample text data file\n",
#     "this is the third line of text\n",
#     "this is the fourth line\n"
# ]
#
# file.writelines(text_lines)
# file.close()
#
# file = open("data2.txt", "r")
# char = file.readlines()
# print(char)