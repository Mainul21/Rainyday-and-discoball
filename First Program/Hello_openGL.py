from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


direction = 0 #right gele add, left gele subtract, ekhon soja ache
background = True

def draw_triangle(x1, y1,x2,y2,x3,y3):
# Eikhnae Chaader jonnno triangle draw kora hoise
    glPointSize(50) #pixel size. by default 1 thake
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2) #jekhane show korbe pixel

    glVertex2f(x2,y2) #jekhane show korbe pixel
    glVertex2f(x3,y3) #jekhane show korbe pixel
    
    glVertex2f(x3,y3) #jekhane show korbe pixel
    glVertex2f(x1,y1) #jekhane show korbe pixel
    
    glEnd()

def draw_rectangle(x1, y1,x2,y2,x3,y3,x4,y4):
    # eikhnae nicher rectangle ta draw kora hoise
    glPointSize(50) #pixel size. by default 1 thake
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2) #jekhane show korbe pixel

    glVertex2f(x2,y2) #jekhane show korbe pixel
    glVertex2f(x3,y3) #jekhane show korbe pixel
    
    glVertex2f(x3,y3) #jekhane show korbe pixel
    glVertex2f(x4,y4) #jekhane show korbe pixel
    
    glVertex2f(x4,y4) #jekhane show korbe pixel
    glVertex2f(x1,y1) #jekhane show korbe pixel
    
    glEnd()

def draw_door(x1, y1,x2,y2,x3,y3,x4,y4):
    # eikhnae nicher rectangle ta draw kora hoise
    glPointSize(50) #pixel size. by default 1 thake
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2) #jekhane show korbe pixel

    glVertex2f(x2,y2) #jekhane show korbe pixel
    glVertex2f(x3,y3) #jekhane show korbe pixel
    
    glVertex2f(x3,y3) #jekhane show korbe pixel
    glVertex2f(x4,y4) #jekhane show korbe pixel
    
    glVertex2f(x4,y4) #jekhane show korbe pixel
    glVertex2f(x1,y1) #jekhane show korbe pixel
    
    glEnd()

def draw_window(x1, y1,x2,y2,x3,y3,x4,y4):
    # eikhnae nicher rectangle ta draw kora hoise
    glPointSize(50) #pixel size. by default 1 thake
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2) #jekhane show korbe pixel

    glVertex2f(x2,y2) #jekhane show korbe pixel
    glVertex2f(x3,y3) #jekhane show korbe pixel
    
    glVertex2f(x3,y3) #jekhane show korbe pixel
    glVertex2f(x4,y4) #jekhane show korbe pixel
    
    glVertex2f(x4,y4) #jekhane show korbe pixel
    glVertex2f(x1,y1) #jekhane show korbe pixel
    
    glEnd()

def draw_rain():
    global direction, background
    if background == True:#House and rain color change
        glColor3f(0.0, 0.0, 0.0)
    else:
          glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2.5)
    glutPostRedisplay()
    for _ in range(200):  
        x = random.randint(0, 500)  
        y = random.randint(0, 500)  
        glBegin(GL_LINES)
        glVertex2f(x, y)  
        glVertex2f(x+(5*direction), y-20)  
        glEnd()

def draw_house():
    # Rectangle ar triangle ta re jora diya ghor banaisi
    draw_triangle(50, 250, 450, 250, 250, 400)
    draw_rectangle(70,250,70,50,430,50,430,250)
    draw_door(140,150,140,50,200,50,200,150)
    draw_window(240,200,240,130,320,130,320,200)



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global background
    if background == True:
        glClearColor(1.0, 1.0, 1.0, 1.0)
    else:
        glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(0.0, 0.0, 0.0) #ghor color korse #konokichur color set (RGB)
    #call the draw methods here
    draw_rain()
    draw_house() #eikhane call hoise function ta
    

    glutSwapBuffers()

def specialKeyListener(key, x, y):
    global direction
    if key == GLUT_KEY_RIGHT:
        direction = 1  
        print("to the right")
    elif key == GLUT_KEY_LEFT:
        direction = -1  
        print("to the left")
    elif key == GLUT_KEY_DOWN:
        direction = 0 
        print("Down")

def keyboardListener(key,x,y):
    global background

    if key == b"d":
        background = True
        print("It's day time")
    elif key ==b"n":
        background = False
        print("It's night time")


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)


glutMainLoop()

