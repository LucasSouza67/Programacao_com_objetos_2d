from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random


# ========================= Classe Base ========================= #
class Shape:

    def __init__(self, x, y, color):

        self.x = x
        self.y = y
        self.color = color

        self.vertices = []
        self.indices = []

    def draw(self):

        glColor3f(*self.color)

        glBegin(GL_TRIANGLES)

        for index in self.indices:
            vx, vy = self.vertices[index]

            glVertex2f(vx + self.x, vy + self.y)

        glEnd()


# ========================= Quadrado ========================= #
class Square(Shape):

    def __init__(self, x, y, size, color):

        super().__init__(x, y, color)

        s = size / 2

        # Shared vertex
        self.vertices = [
            (-s,  s),   # v0
            ( s,  s),   # v1
            ( s, -s),   # v2
            (-s, -s)    # v3
        ]

        self.indices = [
            0, 1, 2,
            2, 3, 0
        ]


# ========================= Triângulo ========================= #
class Triangle(Shape):

    def __init__(self, x, y, size, color):

        super().__init__(x, y, color)

        s = size

        self.vertices = [
            (0, s),
            (-s, -s),
            (s, -s)
        ]

        self.indices = [
            0, 1, 2
        ]


# ========================= Hexágono ========================= #
class Hexagon(Shape):

    def __init__(self, x, y, radius, color):

        super().__init__(x, y, color)

        # Centro
        self.vertices.append((0, 0))

        # Vértices externos
        for i in range(6):

            angle = math.radians(i * 60)

            vx = radius * math.cos(angle)
            vy = radius * math.sin(angle)

            self.vertices.append((vx, vy))

        # Triângulos
        for i in range(1, 7):

            next_i = i + 1 if i < 6 else 1

            self.indices.extend([
                0, i, next_i
            ])


# ========================= Círculo ========================= #
class Circle(Shape):

    def __init__(self, x, y, radius, color, segments=30):

        super().__init__(x, y, color)

        # Centro
        self.vertices.append((0, 0))

        # Circunferência
        for i in range(segments):

            angle = 2 * math.pi * i / segments

            vx = radius * math.cos(angle)
            vy = radius * math.sin(angle)

            self.vertices.append((vx, vy))

        # Índices
        for i in range(1, segments):

            self.indices.extend([
                0, i, i + 1
            ])

        self.indices.extend([
            0, segments, 1
        ])


# ========================= Lista de formas ========================= #
shapes = []


# ========================= Display ========================= #
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    for shape in shapes:
        shape.draw()

    glutSwapBuffers()


# ========================= Inicialização ========================= #
def init():

    glClearColor(0.1, 0.1, 0.1, 1)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(-100, 100, -100, 100)


# ========================= Main ========================= #
def main():

    global shapes

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(800, 800)

    glutCreateWindow(b"Painel das Formas")

    init()

    # ========================= Formas ========================= #

    shapes = [

        Square(
            x=-50,
            y=50,
            size=40,
            color=(1, 0, 0)
        ),

        Triangle(
            x=50,
            y=50,
            size=25,
            color=(0, 1, 0)
        ),

        Circle(
            x=-50,
            y=-50,
            radius=20,
            color=(0, 0, 1)
        ),

        Hexagon(
            x=50,
            y=-50,
            radius=20,
            color=(1, 1, 0)
        )
    ]

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()