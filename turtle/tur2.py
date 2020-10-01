import turtle
for i in range(9):
	turtle.circle((i+1)*30)
	turtle.pu()
	turtle.seth(-90)
	turtle.fd(30)
	turtle.seth(0)
	turtle.pd()
