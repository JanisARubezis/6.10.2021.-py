fails=open('fails1.txt', 'a')
for i in range(10):
    fails.write('hhweuwehbrh %d\r\n' % (i+1))
#print(fails.read())
fails.close()