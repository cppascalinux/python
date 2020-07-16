import math
def quadratic(a,b,c):
	r=math.sqrt(b*b-4*a*c)
	x1=(-b+r)/a/2;x2=(-b-r)/a/2
	return x1,x2
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')