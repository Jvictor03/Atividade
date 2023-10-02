"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
#eixo X e Y.

def square(start, end):#quadradro
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
        forward(100)

    end_fill()#fim
#acrecentei o forward(100)

def circle(start, end):#circulo
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(10):
        forward(end.x - start.x)
        forward(2)
        left(1)
        forward(20)
        left(40)
       #codigo do circulo
       
    end_fill()#fim

def rectangle(start, end):#retangulo

    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
        forward(60)
        left(90)
        forward(100)
    #acrecentei dois forward um de (60) e outro de(100).
    end_fill()#fim


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)
        forward(100)
       
    end_fill()#fim
#acrecentei um left de (120) e um forward(100)

def hexagon(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(8):
        forward(end.x - start.x)
        forward(50)
        left(60)
        forward(50)
    #fizemos um hexogono
    end_fill()#fim


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value
#não mexer 

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store ('shape',hexagon),'h')
done()
#mudei a cor coloquei o white no W. e green no G.