from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import datetime

FONT_DOWNSCALE = 0.005
x = []
y = []
n = 60

now = datetime.datetime.now()
sec = now.second
min = now.minute
hour = (now.hour % 12) * 5


def InitGL(Width, Height):
    glClearColor(0.2, 0.2, 0.2, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, Width / Height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw():
    global x, y, n, sec, min, hour
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # smoothen the picture - make points rounded.
    glEnable(GL_ALPHA_TEST)
    glAlphaFunc(GL_NOTEQUAL, 0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_POINT_SMOOTH)

    # start drawing our clock
    circle()
    coordinates()

    for i in range(n):
        if i % 5 != 0:
            vertex(x[i], y[i])
        else:
            vertex_hour(x[i], y[i])

    draw_text('12', x[0] - 0.4, y[0] - 0.2)
    draw_text('1', x[5], y[5])
    draw_text('2', x[10], y[10] - 0.1)
    draw_text('3', x[15], y[15] - 0.3)
    draw_text('4', x[20], y[20] - 0.3)
    draw_text('5', x[25], y[25] - 0.3)
    draw_text('6', x[30] - 0.2, y[30] - 0.3)
    draw_text('7', x[35] - 0.3, y[35] - 0.3)
    draw_text('8', x[40] - 0.2, y[40] - 0.4)
    draw_text('9', x[45] - 0.3, y[45] - 0.2)
    draw_text('10', x[50] - 0.3, y[50])
    draw_text('11', x[55] - 0.2, y[55])

    vertex(0, 0)

    glColor(1, 0, 0)
    hand(x[sec] * 0.95, y[sec] * 0.95, 5)  # seconds hand

    x_minute = x[min] * 0.8  # hand length
    y_minute = y[min] * 0.8
    glColor(1, 1, 1)
    hand(x_minute, y_minute, 5)  # minutes hand

    x_hour = x[hour] * 0.5  # hand length
    y_hour = y[hour] * 0.5
    glColor(0.3, 0.4, 1)
    hand(x_hour, y_hour, 13)  # hour hand

    now = datetime.datetime.now()
    sec = now.second
    min = now.minute
    hour = (now.hour % 12) * 5
    glutSwapBuffers()


# Outer circle
def circle():
    glColor(0.14, 0.14, 0.14)
    glTranslate(0, 0, -4.63)
    glScale(1.1, 1.08, 1)
    glutSolidSphere(1.5, 100, 100)
    glFlush()


# vertices of minutes and center vertex
def vertex(x, y):
    glLoadIdentity()
    glTranslate(0, 0, -9)
    glColor(0.3, 0.4, 1)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex(x, y)
    glEnd()
    glFlush()


# vertices of hours
def vertex_hour(x, y):
    glLoadIdentity()
    glTranslate(0, 0, -9)
    glColor(1, 1, 1)
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex(x, y)
    glEnd()
    glFlush()


# generate coordinates for the vertices
def coordinates():
    global x, y, n
    radius = 3
    for i in range(n):
        x.append(radius * sin(2.0 * pi * i / n))
        y.append(radius * cos(2.0 * pi * i / n))


# hour / minute / seconds hands
def hand(x, y, width):
    glLoadIdentity()
    glTranslate(0, 0, -9)
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex(x, y)
    glVertex(0, 0)
    glEnd()
    glFlush()


# To draw the numbers 1-12
def draw_text(string, x, y):
    glLineWidth(3)
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslate(x, y, -2.2)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE,
            1)  # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    glColor(1, 1, 1)
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()


def timer(v):
    draw()
    glutTimerFunc(10, timer, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Clock')
    glutDisplayFunc(draw)
    glutTimerFunc(10, timer, 1)
    InitGL(600, 500)
    glutMainLoop()


main()
