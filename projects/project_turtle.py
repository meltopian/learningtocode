import turtle  # https://docs.python.org/3.3/library/turtle.html
t = turtle.Pen()

t.speed(0)
turtle.tracer(False)

t.fd(100)

t.goto(50,50)
t.penup()
t.goto(-200,200)
t.pendown()
t.fd(100)

def square(size):
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
def square(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)
# triangle?, pentagon?



def closed_shape(size, num_sides):
    for i in range(num_sides):
        t.fd(size)
        t.lt(360/num_sides)

def filled_shape(size, num_sides, color):
    t.fillcolor(color)
    t.begin_fill()
    closed_shape(size, num_sides)
    t.end_fill()

def circle_test():
    t.circle(120, 180)
    t.begin_fill()
    t.circle(120, 180)
    t.end_fill()

def spirograph(freq, size, sides, color):
    for i in range(freq):
        filled_shape(size, sides, color)
        t.lt(360 / freq)

t.goto(0,0)
t.reset()

breakpoint()  # If using <python3.7: import pdb ; pdb.set_trace()