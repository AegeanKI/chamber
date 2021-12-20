from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from stl import mesh

def showSTL(filename):
    points, faces = loadSTL(filename)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    for face in faces:
        for f in face:
            vertexDraw = points[int(f) - 1]

            if int(f) % 3 == 1:
                glColor4f(0.282, 0.239, 0.545, 0.35)
            elif int(f) % 3 == 2:
                glColor4f(0.729, 0.333, 0.827, 0.35)
            else:
                glColor4f(0.545, 0.000, 0.545, 0.35)
            glVertex3fv(vertexDraw)
    glEnd() 

def loadSTL(filename):
    m = mesh.Mesh.from_file(filename)
    shape = m.points.shape
    points = m.points.reshape(-1, 3)
    faces = np.arange(points.shape[0]).reshape(-1, 3)
    return points, faces
 
def reshape(width, height):
    gluLookAt(0, 1355, -20, 0, 0, -20, 0, 1, 0)
    gluPerspective(60, (600/600), 0.1, 1500.0)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotatef(0.1, 10,5,0)
    
    # glutWireTeapot(1)
    showSTL("data/chamber.stl")

    glFlush()
 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowPosition(400,200)
    glutInitWindowSize(600,600)
    glutCreateWindow("test")
    glutDisplayFunc(drawFunc)
    glutReshapeFunc(reshape)
    # glutIdleFunc(drawFunc)
    glutMainLoop()

if __name__ == "__main__":
    main()
