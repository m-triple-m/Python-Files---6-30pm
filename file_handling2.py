import os

# try:
#     f = open('./myfolder/testing.txt')

#     f.write('sentence 1')

#     print(f.read())

# finally:
#     f.close()


with open('./myfolder/testing.txt', 'r+') as f:
    print(f.readline())
    print(f.readline())
    print(f.write('\n Sentence 2'))