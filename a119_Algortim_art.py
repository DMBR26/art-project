import turtle as trtl

painter = trtl.Turtle()
trtl.tracer(0,0)

# Canvas 

# Spiral or Galaxy 
color1 = "purple"
color2 = "blue"

wn = trtl.Screen()
height = 800 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(20)
painter.color(color1)

space = 5
angle = 65 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  if (space % 200 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  elif (space % 100 == 0):
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.forward(1*space + 5) # experiment
  painter.begin_fill()
  painter.circle(2)
  painter.end_fill()
  space += 1


# CoolGuy/Thing Outline
painter.pencolor("black")
painter.pensize(10)
painter.penup()
painter.goto(-170, 170)
painter.pendown()
painter.goto(0,-200)
painter.goto(170,170)
painter.goto(-170,170)
painter.goto(-160,150)
painter.goto(162,150)
painter.penup()

# Parts 
painter.goto(20,30)
painter.pendown()
painter.pencolor("red")
painter.pensize(25)
painter.goto(20,31)

painter.penup()
painter.goto(50,20)
painter.pendown()
painter.goto(50,21)
painter.penup()


painter.speed(0)
painter.pensize(1)
# other
# starting location of the tower
x = -170
y = -50

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("yellow")
    
  y = y + 5 # location of next floor
   
  #draw the floor
  painter.pendown()
  painter.forward(100)


trtl.update
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()