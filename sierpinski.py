import turtle
import math

def teleport(koopa, pos):
  koopa.hideturtle()
  koopa.up()
  koopa.setpos(pos)
  koopa.down()
  koopa.showturtle()

def draw_triangle(koopa, pos, length, angle, color):
  teleport(koopa, pos)
  koopa.setheading(0)
  koopa.right(30)

  koopa.fill(True)
  koopa.fillcolor(color)
  for i in range(3):
    koopa.forward(length)
    koopa.right(angle)
  koopa.fill(False)


def sierpinski(koopa, pos, length, level):
  draw_triangle(koopa, pos, length, -120, "white")

  if level > 0:
    sierpinski(koopa, (pos[0], pos[1] + length * math.sin(math.radians(60))), length/2, level-1)
    sierpinski(koopa, (pos[0]-length/2, pos[1]), length/2, level-1)
    sierpinski(koopa, (pos[0]+length/2, pos[1]), length/2, level-1)

def main():
  window = turtle.Screen()
  window.bgcolor("black")

  turtle.mode("logo")

  koopa = turtle.Turtle()
  koopa.shape("classic")
  koopa.color("#028482","#028482")
  koopa.speed(1000)

  # The board/background
  draw_triangle(koopa, (-300,-300), 600, 120, "#028482")
  # The actual Sierpinski Triangle
  sierpinski(koopa, (0, -300), 300, 3)

  window.exitonclick()

main()