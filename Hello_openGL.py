from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x1, y1,x2,y2,x3,y3):
    glPointSize(1) #pixel size. by default 1 thake
    # x1, x2, x3 = 200,400,300
    # y1,y2,y3 = 250,250,400
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2) #jekhane show korbe pixel

    glVertex2f(x2,y2) #jekhane show korbe pixel
    glVertex2f(x3,y3) #jekhane show korbe pixel
    
    glVertex2f(x3,y3) #jekhane show korbe pixel
    glVertex2f(x1,y1) #jekhane show korbe pixel

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(200, 250, 400, 250, 300, 400)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

# for drawing hollow traiangle use the GL.LINES function