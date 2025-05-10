import os

path = 'c:\\Users\\golol\\Downloads\\Logo'
#path = 'c:/Users/golol/Downloads/Logo'

path = os.path.normpath(path)
# print(path)

# for path, dirnames, filenames in os.walk(path):
#     print(path)
#     print(dirnames)
#     print(filenames)

# dir = "Test2"
# path = os.path.join(path, dir)
# os.mkdir(path)
# print(path)

# path = 'c:\\Users\\golol\\Downloads\\Logo\\Python-logo.png'
# print(os.path.isabs(path))
# print(os.path.isdir(path))
# print(os.path.isfile(path))
# print(os.path.exists(path))
# print(os.path.getsize(path))
# print(os.path.getatime(path))

# f = open("test.txt", 'w')
# f.write("hello python")
# f.close()

# f = open("test.txt", 'r')
# st = f.read()
# f.close()
# print(st)

path = 'c:\\Users\\golol\\Downloads\\Logo\\'

def spy(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("spy.txt", "w", encoding='utf-8') as f:
        for dir in result["dirs"]:
            f.write(f"[{dir.upper()}]\n")
        for file in result["files"]:
            f.write(f"{file}\n")


spy(path)

#Привіт пайтон!