file = open('BANJIHYUN.txt', 'rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')
    
file.close()