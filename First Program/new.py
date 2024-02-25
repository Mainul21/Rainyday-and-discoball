from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

raindrops = [[0.2, 0.8], [0.4, 0.7], [0.6, 0.6], [0.8, 0.5]]

def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()

def draw_rectangle(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glVertex2f(x4, y4)
    glVertex2f(x1, y1)
    glEnd()

def draw_door(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glVertex2f(x4, y4)
    glVertex2f(x1, y1)
    glEnd()

def draw_window(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glVertex2f(x4, y4)
    glVertex2f(x1, y1)
    glEnd()

def draw_house():
    draw_triangle(50, 250, 450, 250, 250, 400)
    draw_rectangle(70, 250, 70, 50, 430, 50, 430, 250)
    draw_door(140, 150, 140, 50, 200, 50, 200, 150)
    draw_window(240, 200, 240, 130, 320, 130, 320, 200)

def draw_raindrop(x, y):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y - 0.02)  # Adjust length of raindrop
    glEnd()

def draw_rain():
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue for raindrops
    for drop in raindrops:
        draw_raindrop(*drop)

def update_rain():
    for i in range(len(raindrops)):
        raindrops[i][1] -= 0.01  # Adjust the speed of raindrops
        if raindrops[i][1] < -1.0:
            raindrops[i] = [random.uniform(0.0, 1.0), 1.0]  # Reset raindrop if it goes below the screen

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0)
    draw_house()

    # Draw rain after drawing the house
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue for raindrops
    for drop in raindrops:
        draw_raindrop(*drop)

    update_rain()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    iterate()

    # Initialize raindrops with random positions
    for _ in range(100):
        raindrops.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])

    glutMainLoop()

if __name__ == "__main__":
    main()
