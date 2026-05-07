from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random


# ========================= Classe Base ========================= #
class Shape:

    def __init__(self, x, y, color):

        self.x = x
        self.y = y

        self.color = color

        self.vertices = []
        self.indices = []

    # ========================= Desenho ========================= #
    def draw(self):

        glColor3f(*self.color)

        glBegin(GL_TRIANGLES)

        for index in self.indices:

            vx, vy = self.vertices[index]

            glVertex2f(vx + self.x, vy + self.y)

        glEnd()


# ========================= Triângulo Isósceles ========================= #
class IsoscelesTriangle(Shape):

    def __init__(self, x, y, base, height, color):

        super().__init__(x, y, color)

        half_base = base / 2
        half_height = height / 2

        # Shared vertex
        self.vertices = [

            (0, half_height),                 # topo

            (-half_base, -half_height),      # esquerda

            (half_base, -half_height)        # direita
        ]

        # Índices
        self.indices = [
            0, 1, 2
        ]


# ========================= Cor Aleatória ========================= #
def random_color():

    return (
        random.random(),
        random.random(),
        random.random()
    )


# ========================= Lista de Triângulos ========================= #
triangles = []


# ========================= Display ========================= #
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    for triangle in triangles:
        triangle.draw()

    glutSwapBuffers()


# ========================= Inicialização ========================= #
def init():

    glClearColor(0.05, 0.05, 0.05, 1)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(-100, 100, -100, 100)


# ========================= Criar Triângulo ========================= #
def create_triangle():

    base = float(input("Digite a base do triângulo: "))
    height = float(input("Digite a altura do triângulo: "))

    return base, height


# ========================= Programa Principal ========================= #
def main():

    global triangles

    # Entrada do usuário
    base, height = create_triangle()

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(800, 800)

    glutCreateWindow(b"Triangulos Isosceles")

    init()

    # ========================= Cena ========================= #

    triangles = [

        IsoscelesTriangle(
            x=-70,
            y=60,
            base=base,
            height=height,
            color=random_color()
        ),

        IsoscelesTriangle(
            x=0,
            y=60,
            base=base * 0.7,
            height=height * 1.2,
            color=random_color()
        ),

        IsoscelesTriangle(
            x=70,
            y=50,
            base=base * 1.5,
            height=height * 0.8,
            color=random_color()
        ),

        IsoscelesTriangle(
            x=-40,
            y=-40,
            base=base * 0.5,
            height=height * 0.5,
            color=random_color()
        ),

        IsoscelesTriangle(
            x=50,
            y=-50,
            base=base * 1.2,
            height=height * 1.5,
            color=random_color()
        )
    ]

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()