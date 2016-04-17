import turtle

def draw_pedal(turtle):
  for i in range(2):
    turtle.forward(100)
    turtle.right(60)
  turtle.right(60)
  for i in range(2):
    turtle.forward(100)
    turtle.right(60)

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("black")

  maturin = turtle.Turtle()
  maturin.shape("turtle")
  maturin.color("#028482","#028482")
  maturin.speed(1000)

  for i in range(90):
    draw_pedal(maturin)
    maturin.right(4)

  maturin.right(90)
  maturin.forward(250)

  window.exitonclick()

draw_flower()