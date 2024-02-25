from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500
points = []
speed = 0.5
flag = True

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])] #selecting direction randomly

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a, b

def draw_point(x, y, color):
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glEnd()

def draw_boundary():
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-W_Width/4, W_Height/4)
    glVertex2f(W_Width/4, W_Height/4)
    glVertex2f(W_Width/4, -W_Height/4)
    glVertex2f(-W_Width/4, -W_Height/4)
    glEnd()

def generate_random_point(x, y):
    color = (random.random(), random.random(), random.random())#getting the points between 0.0 t0 1.0
    return Point(x, y, color)

def mouseListener(button, state, x, y):
    global points
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        x, y = convert_coordinate(x, y)
        print(x+W_Width/2,y+W_Height/2)
        points.append(generate_random_point(x, y))

def specialKeyListener(key,x,y):
    global speed
    if key == GLUT_KEY_DOWN:
        speed-=0.1
    elif key == GLUT_KEY_UP:
        speed+=0.1
def keyboardListener(key,x,y):
    global flag

    count = 0

    if key == b" " and count%2==0:
        flag = False
        count+=1
    elif key == b" " and count%2 != 0:
        flag = True
        count+=1


def animate_points():
    global points, W_Width, W_Height, speed, flag
    if flag == True:
        for point in points:
            point.x += 2 * speed * point.direction[0]
            point.y += 2 * speed * point.direction[1]

            # Check boundary collision
            if abs(point.x) >= W_Width/4:
                point.direction[0] *= -1
            if abs(point.y) >= W_Height/4:
                point.direction[1] *= -1
    else:
        for point in points:
            point.x += 2 * 0 * point.direction[0]
            point.y += 2 * 0 * point.direction[1]

            # Check boundary collision
            if abs(point.x) >= W_Width/4:
                point.direction[0] *= -1
            if abs(point.y) >= W_Height/4:
                point.direction[1] *= -1

def showScreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_boundary()

    for point in points:
        draw_point(point.x, point.y, point.color)

    animate_points()
    glutSwapBuffers()

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-W_Width/2, W_Width/2, -W_Height/2, W_Height/2)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()
