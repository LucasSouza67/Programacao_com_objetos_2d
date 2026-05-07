from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


# ========================= Classe do Retângulo ========================= #
class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.color = self.random_color()

        # ========================= Shared Vertex ========================= #
        self.vertices = [
            (-width / 2,  height / 2),  # v0
            ( width / 2,  height / 2),  # v1
            ( width / 2, -height / 2),  # v2
            (-width / 2, -height / 2)   # v3
        ]

        # Índices
        self.indices = [
            0, 1, 2,
            2, 3, 0
        ]

    # ========================= Cor aleatória ========================= #
    def random_color(self):
        return (
            random.random(),
            random.random(),
            random.random()
        )

    # ========================= Atualizar cor ========================= #
    def update_color(self):
        self.color = self.random_color()

    # ========================= Desenhar ========================= #
    def draw(self):

        glColor3f(*self.color)

        glBegin(GL_TRIANGLES)

        for index in self.indices:
            glVertex2f(*self.vertices[index])

        glEnd()


# ========================= Variáveis globais ========================= #
rect = None

bg_color = (0.0, 0.0, 0.0)


# ========================= Display ========================= #
def display():

    glClearColor(*bg_color, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    rect.draw()

    glutSwapBuffers()


# ========================= Teclado ========================= #
def keyboard(key, x, y):

    global bg_color

    # Barra de espaço
    if key == b' ':

        rect.update_color()

        bg_color = (
            random.random(),
            random.random(),
            random.random()
        )

        glutPostRedisplay()


# ========================= Inicialização ========================= #
def init():

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(-100, 100, -100, 100)


# ========================= Programa principal ========================= #
def main():

    global rect

    width = float(input("Digite a largura do retângulo: "))
    height = float(input("Digite a altura do retângulo: "))

    rect = Rectangle(width, height)

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(600, 600)

    glutCreateWindow(b"Retangulo do Caos")

    init()

    glutDisplayFunc(display)

    glutKeyboardFunc(keyboard)

    glutMainLoop()


if __name__ == "__main__":
    main()