def findMinAndMax(L):
	if len(L)==0:
		return None,None
	mn=L[0]
	mx=L[0]
	for i in L:
		mn=min(mn,i);
		mx=max(mx,i);
	return mn,mx
	# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')