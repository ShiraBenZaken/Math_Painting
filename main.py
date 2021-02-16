from canvas import Canvas
from rectangle import Rectangle
from square import Square


print('Hello and Welcome to Math Painting ')
# Canvas width and height
canvas_height = int(input("Enter canvas height "))
canvas_width = int(input("Enter canvas width "))
# Choose Color
colors = {"white" : (255, 255, 255) , "black" : (0, 0, 0)}
canvas_color = input("Enter your canvas color (white or black) ")

# Create a canvas with User data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True:
    shape_type = input("What do u want to draw ? Enter Quit to Quit ")
    if shape_type.lower() == 'quit':
        break
    # Ask if its Rectangle
    elif shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x for Rectangle "))
        rec_y = int(input("Enter y for Rectangle "))
        rec_width = int(input("Enter width for Rectangle "))
        rec_height = int(input("Enter height for Rectangle "))
        red = int(input("How mach red do u like in the Rectangle "))
        green = int(input("How mach green "))
        blue = int(input("How mach blue "))
        # Create the Rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=[red, green, blue])
        r1.draw(canvas)
    elif shape_type.lower() == 'square':
        sqr_x = int(input("Enter x for Square "))
        sqr_y = int(input("Enter y for Square "))
        sqr_side = int(input("Enter side lenght for Square "))
        red = int(input("How mach red do u like in the Rectangle "))
        green = int(input("How mach green "))
        blue = int(input("How mach blue "))
        # Create the Square
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=[red, green, blue])
        s1.draw(canvas)

canvas.make('canvas.png')




