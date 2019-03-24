from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    gluPerspective(60,1,0.1,50)
    gluLookAt(8,9,10,
               0,0,0,
               0,1,0)
    glClearColor(0.3,0.4,0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    
def draw_axises():
    glBegin(GL_LINES)
    glColor3f(1.0, 0, 0)
    glVertex(0,0,0)
    glVertex(10,0,0)
    
    glColor3f(0, 1, 0)
    glVertex(0,0,0)
    glVertex(0,10,0)
    glColor3f(0, 0,1)
    glVertex(0,0,0)
    glVertex(0,0,10) 
    glEnd()

def draw_Road():
    glBegin(GL_QUADS)
    #GRAY
    glColor3f(0.5,0.5,0.4)
    glVertex(-50,0,-5)
    glVertex(-50,0,4)  
    glVertex(20,0,4)
    glVertex(20,0,-5)
    # كبير
    glColor3f(0.6,0.6,0.5)
    glVertex(-40,0,-5)
    glVertex(-40,0,-8)
    glVertex(20,0,-8)
    glVertex(20,0,-5)

    glVertex(-40,0,4)
    glVertex(-40,0,5)
    glVertex(20,0,5)
    glVertex(20,0,4)
    # صغير
    glColor3f(0.4,0.4,0.3)
    glVertex(-40,0,-5)
    glVertex(-40,0,-5.5)
    glVertex(20,0,-5.5)
    glVertex(20,0,-5)

    glVertex(-40,0,4)
    glVertex(-40,0,4.2)
    glVertex(20,0,4.2)
    glVertex(20,0,4)
#WHITE
    glColor3f(1,1,1)
    glVertex(-18,0,0.5)
    glVertex(-18,0,1)
    glVertex(-15,0,1)
    glVertex(-15,0,0.5)
    
    glVertex(-8,0,0.5)
    glVertex(-8,0,1)
    glVertex(-5,0,1)
    glVertex(-5,0,0.5)
    
    glVertex(-1,0,0.5)
    glVertex(-1,0,1)
    glVertex(2,0,1)
    glVertex(2,0,0.5)

    glVertex(5,0,0.5)
    glVertex(5,0,1)
    glVertex(7,0,1)
    glVertex(7,0,0.5)    
    glEnd()
    glLineWidth(3)

    glBegin(GL_LINES)
    glColor3f(0.3,0.3,0.2)
    for i in range (-40,50,4):
        glVertex(i,0,-5.5)
        glVertex(i,0,-8)
        glVertex(i,0,4.20)
        glVertex(i,0,5)
        i+=3
    glEnd()

def draw_TREE():
    # عشب
    for i in range(-40,50,2):
        glBegin(GL_LINES)
        glColor3f(0.5,0.7,0.1)
        glVertex(i,0,6.1)
        glVertex(i,0,5.9)
        glVertex(i,0,6.9)
        glVertex(i,0,6.7)
        glVertex(i,0,7.7)
        glVertex(i,0,7.5)
        glVertex(i,0,8.5)
        glVertex(i,0,8.3)
        glEnd()
    for i in range(-40,50,1):
        glBegin(GL_LINES)
        glColor3f(0.5,0.7,0.1)
        glVertex(i,0,6.5)
        glVertex(i,0,6.3)
        glVertex(i,0,7.3)
        glVertex(i,0,7.1)
        glVertex(i,0,8.1)
        glVertex(i,0,7.9)
        glVertex(i,0,8.9)
        glVertex(i,0,8.7)
        glEnd()

    for i in range(-40,50,2):
        glBegin(GL_LINES)
        glColor3f(0.5,0.7,0.1)
        glVertex(i,0,-15.1)
        glVertex(i,0,-14.9)
        glVertex(i,0,-15.9)
        glVertex(i,0,-15.7)
        glVertex(i,0,-16.7)
        glVertex(i,0,-16.5)
        glVertex(i,0,-17.5)
        glVertex(i,0,-17.3)
        glEnd()
    for i in range(-40,50,1):
        glBegin(GL_LINES)
        glColor3f(0.5,0.7,0.1)
        glVertex(i,0,-15.5)
        glVertex(i,0,-15.3)
        glVertex(i,0,-16.3)
        glVertex(i,0,-16.1)
        glVertex(i,0,-17.1)
        glVertex(i,0,-16.9)
        glVertex(i,0,-17.9)
        glVertex(i,0,-17.7)
        glEnd()
    #TREE
    for i in range(-30,40,15):
        glLoadIdentity()
        glTranslate(-i,0,-15)
        glScale(1,8,1)
        glColor3f(0.5,0.2,0)
        glutSolidCube( 0.5 )
    
        glLoadIdentity()
        glTranslate(-i,3,-15)
        glRotate(-90,1,0,0)
        glColor3f(0.5,0.7,0.2)
        glScale(1.5,1.5,1.5)
        #glutSolidIcosahedron( )
        #glutSolidDodecahedron( )
        glutWireSphere(1.5 , 15 , 15)
            
angle=0
x=0
forward=True
def display():
    global angle
    global x
    global forward
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #draw_axises()
    draw_Road()
    draw_TREE()
#TORUS 
    glLoadIdentity()
    glTranslate(2.5,-2.5*0.25,-0.5*2.5)
    glTranslate(x,0,0)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )

    glLoadIdentity()
    glTranslate(-2.5,-2.5*0.25,-0.5*2.5)
    glTranslate(x,0,0)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )
#CUBE
    glLoadIdentity()
    glColor3f(0.4,0,0.1) 
    glTranslate(x,0,0)
    glScale( 1,0.25 ,0.5 )
    glutSolidCube(5)    
    
    glLoadIdentity()
    glTranslate(x,5*0.25,0)
    glScale( .5,0.25 ,.5) 
    glutSolidCube(5)      
#TORUS
    glLoadIdentity()
    glTranslate(2.5,-2.5*0.25,0.5*2.5)
    glTranslate(x,0,0)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )
    
    glLoadIdentity()
    glTranslate(-2.5,-2.5*0.25,0.5*2.5)
    glTranslate(x,0,0)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )
#SPHERE
    glLoadIdentity()
    glColor3f(0.9,1,0.1)
    glTranslate(2.58,-2.5*0.25,0.25*1)
    glTranslate(x,0,0)
    glutWireSphere(.25 , 10 , 10)

    glLoadIdentity()
    glColor3f(0.9,1,0.1)
    glTranslate(2.58,-2.5*0.25,-0.25*4.5)
    glTranslate(x,0,0)
    glutWireSphere(.25 , 10 , 10)
    glLoadIdentity()
#CAR DESIGN
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(1.0,2.5*0.25,-0.5*1)
    glTranslate(x,0,0)
    glScale( 0,0.2,0.5 )
    glutSolidCube(5)
    #problem 
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-0.9,-0.8,-0.7)#-0.8 0.7
    glTranslate(x,0,0)
    glScale( 0.3 ,0.2,0 )
    glutSolidCube(5)
    
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-2.5,-0.8,-0.7)
    glTranslate(x,0,0)
    glScale( 0.3 ,0.2,0 )
    glutSolidCube(5)

    if forward:
         angle -= 0.1
         x += .06
         if x>5:
             forward = False
        
    else:
         angle += 0.1
         x -= .06
         if x<-10:
             forward = True
      
    glutSwapBuffers()

    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b'Moving Car')
glutDisplayFunc(display)
#glutIdleFunc(display)
myInit()
glutMainLoop()    
