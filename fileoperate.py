__author__ = 'fengjigang'
# file = open('./haha.txt','w')
# file.write('1')
# file.write('2')
# file.write('3456789')
# file.seek(5)
# file.write('abcdefg')
# file.flush()
# file = open('./haha.txt','r')
# print file.read

# file = open('./haha.txt')
# print file.read(4)
# print file.read(4)
# print file.read()
# for i in range(3):
#     print file.readline()
# print file.readlines()

# while True:
#     char = file.read(1)
#     if not char:break
#     print char

# while True:
#     line = file.readline()
#     if not line:break
#     print line
# for line in file.readlines():
#     print line

for line in list(open('./haha.txt')):
    print line
# file.close()