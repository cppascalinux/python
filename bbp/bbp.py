from decimal import *
getcontext().prec=10000
i=Decimal('0')
ans=Decimal('0')
while i<10000:
	ans+=1/16**i*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
	i+=1 
print(ans)
