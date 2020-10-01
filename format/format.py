import time
leng=50
print('开始执行'.center(leng,'-'))
t=time.time()
for i in range(101):
	a='*'*(i//2)
	b='.'*(50-i//2)
	print("\r{}%[{}->{}] {:.2f}s".format(i,a,b,(time.time()-t)),end='')
	time.sleep(0.1)
print('\n'+'执行完毕'.center(leng,'-'))
while 1:
	for i in ['/','-','|','\\','|']:
		print("{}\r".format(i),end='')