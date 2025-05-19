import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)

daisy = turtle.Turtle()
daisy.shape("turtle")
daisy.color("red")
daisy.forward(50)
daisy.write(" Daisy")

tom = turtle.Turtle()
tom.shape("Circle")
tom.color("green")
tom.up()
tom.goto(-50, -50)
tom.down()
tom.forward(55)
tom.write(" Tom")

window.mainloop() # is a must be the last line

import random
randomX = random.randint(-150, 150)
randomY = random.randint(100, -100)

# for i in range(6):
#     for inside in range(3):

#         turtle.forward(55)
#         turtle.left(120)

#     turtle.right(60)

# window.mainloop()