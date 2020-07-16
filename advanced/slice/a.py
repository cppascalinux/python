def trim(s):
	lf=0
	rf=-1
	l=len(s)
	for i in range(l):
		if s[i]!=' ':
			rf=i
	for i in range(l-1,-1,-1):
		if s[i]!=' ':
			lf=i
	print('lf:%d rf:%d s:%s '%(lf,rf,s[lf:rf+1]))
	if lf>rf:
		return ''
	return s[lf:rf+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')