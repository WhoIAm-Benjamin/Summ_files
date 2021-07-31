import sys
import os

size = 0
size_folder = 0

def walk(directory, files):
    global size
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            for i in files:
                path1 = path[(path[:].index('.')+1):]
                if path1 == i:
                    try:
                        size += sys.getsizeof(path)
                        print(path, size)
                    except:
                        pass
        else:
            print('Size of folder', directory, sys.getsizeof(directory))
            walk(path, files)

def main():
    # path = os.getcwd()
    path = input('YYYYYYYYYYYYYYYYYYYYYY\n').replace('/', '\\')
    print('YYYYYYYYYYYYYYYYYYYYYY')
    files = input().replace('.', '')
    files = files.split(',')
    k = -1
    for i in files:
        k += 1
        if i[0] == ' ':
            files[k] = i.replace(' ', '')
    walk(path, files)

if __name__ == '__main__':
    main()
