# fp = open('test1.txt','r')
# fp.read()
# fp.close()

try:
    fp = open('test1.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级稍后')