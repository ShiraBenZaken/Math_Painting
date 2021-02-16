class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        # Draw to canvas and slice the array to new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color