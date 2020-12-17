import os

print(os.listdir())

# for f in os.listdir():
#     print(f)

# for p in os.walk('.'):
#     print(p)

# print(os.getcwd())
# os.chdir('./myfolder')
# print(os.getcwd())

# print(os.path.exists('./myfolder'))


os.chdir('c:/Advanced Excel')
for f in os.listdir():
    if os.path.isfile(f):
        # print(f.split('.')[-1])
        r = os.path.realpath(f)
        if os.path.splitext(r)[-1] == '.png':
            print(f)