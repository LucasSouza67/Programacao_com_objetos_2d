from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random


# ========================= Classe Triângulo ========================= #
class Triangle:

    def __init__(self, x, y, base, height, color):

        self.x = x
        self.y = y

        self.base = base
        self.height = height

        self.color = color

        half_base = base / 2
        half_height = height / 2

        # Shared vertex
        self.vertices = [

            (0, half_height),

            (-half_base, -half_height),

            (half_base, -half_height)
        ]

        self.indices = [
            0, 1, 2
        ]

    # ========================= Desenho ========================= #
    def draw(self):

        glColor3f(*self.color)

        glBegin(GL_TRIANGLES)

        for index in self.indices:

            vx, vy = self.vertices[index]

            glVertex2f(vx + self.x, vy + self.y)

        glEnd()

    # ========================= Coordenadas ========================= #
    def get_position_text(self):

        return f"({self.x}, {self.y})"


# ========================= Lista de triângulos ========================= #
triangles = []


# ========================= Desenhar Texto ========================= #
def draw_text(text, x, y):

    glColor3f(1, 1, 1)

    glRasterPos2f(x, y)

    for char in text:

        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_18,
            ord(char)
        )


# ========================= Desenhar Eixos ========================= #
def draw_axes():

    glLineWidth(2)

    glColor3f(1, 1, 1)

    glBegin(GL_LINES)

    # Eixo X
    glVertex2f(-100, 0)
    glVertex2f(100, 0)

    # Eixo Y
    glVertex2f(0, -100)
    glVertex2f(0, 100)

    glEnd()


# ========================= Display ========================= #
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha eixos
    draw_axes()

    # Desenha triângulos
    for triangle in triangles:

        triangle.draw()

        # Texto das coordenadas
        draw_text(
            triangle.get_position_text(),
            triangle.x - 15,
            triangle.y - 25
        )

    glutSwapBuffers()


# ========================= Inicialização ========================= #
def init():

    glClearColor(0.08, 0.08, 0.08, 1)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(-100, 100, -100, 100)


# ========================= Main ========================= #
def main():

    global triangles

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(800, 800)

    glutCreateWindow(b"Plano Cartesiano - Triangulos")

    init()

    # ========================= Triângulos ========================= #

    triangles = [

        # Quadrante I
        Triangle(
            x=50,
            y=50,
            base=20,
            height=30,
            color=(1, 0, 0)
        ),

        # Quadrante II
        Triangle(
            x=-50,
            y=40,
            base=25,
            height=35,
            color=(0, 1, 0)
        ),

        # Quadrante III
        Triangle(
            x=-40,
            y=-50,
            base=30,
            height=25,
            color=(0, 0, 1)
        ),

        # Quadrante IV
        Triangle(
            x=50,
            y=-20,
            base=30,
            height=25,
            color=(1, 0, 1)
        )
    ]

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()