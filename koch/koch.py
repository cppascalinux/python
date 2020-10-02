import turtle
def koch(d):
	l=3**d
	if d<=0:
		turtle.fd(l)
		return
	tr=[60,-120,60,0]
	for i in tr:
		koch(d-1)
		turtle.left(i)
turtle.setup(1080,720)
turtle.pu()
turtle.goto(-500,-300)
turtle.speed(0)
turtle.pd()
koch(int(input()))
turtle.hideturtle()
turtle.exitonclick()