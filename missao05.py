from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random


# ========================= Classe Base ========================= #
class Shape:

    def __init__(self, vertices, color):
        self.vertices = vertices
        self.indices = [0, 1, 2]
        self.color = color

    # ========================= Desenhar ========================= #
    def draw(self):
        glColor3f(*self.color)
        glBegin(GL_TRIANGLES)

        for index in self.indices:
            vx, vy = self.vertices[index]
            glVertex2f(vx, vy)

        glEnd()

    # ========================= Nova Cor ========================= #
    def randomize_color(self):

        self.color = (
            random.random(),
            random.random(),
            random.random()
        )


# ========================= Triângulo ========================= #
class Triangle(Shape):

    def __init__(self, vertices, color):

        super().__init__(vertices, color)

        self.indices = [0, 1, 2]


# ========================= Insígnia de Malta ========================= #
class MaltaInsignia:

    def __init__(self):
        self.triangles = []
        self.create_insignia()

    # ========================= Construção ========================= #
    def create_insignia(self):
        outer_radius = 90   # distância do centro às 8 pontas externas
        notch_radius = 60   # distância do centro ao entalhe em V de cada braço
        half_angle   = 30   # meia largura angular de cada braço (graus)

        color  = self.random_color()
        center = (0.0, 0.0)

        # 4 braços: cima, direita, baixo, esquerda
        arm_directions = [90, 0, -90, 180]

        for arm_dir in arm_directions:
            a_left  = math.radians(arm_dir + half_angle)
            a_right = math.radians(arm_dir - half_angle)
            a_mid   = math.radians(arm_dir)

            tip_left  = (outer_radius * math.cos(a_left),  outer_radius * math.sin(a_left))
            tip_right = (outer_radius * math.cos(a_right), outer_radius * math.sin(a_right))
            notch     = (notch_radius * math.cos(a_mid),   notch_radius * math.sin(a_mid))

            # Dois triângulos por braço formando o V externo
            self.triangles.append(Shape([center, tip_left,  notch],     color))
            self.triangles.append(Shape([center, notch,     tip_right], color))
        
    # ========================= Cor Aleatória ========================= #
    def random_color(self):

        return (
            random.random(),
            random.random(),
            random.random()
        )

    # ========================= Desenhar ========================= #
    def draw(self):
        for tri in self.triangles:
            tri.draw()

    # ========================= Atualizar cores ========================= #
    def energize(self):
        for tri in self.triangles:
            tri.randomize_color()

# ========================= Objeto Global ========================= #
insignia = MaltaInsignia()


# ========================= Display ========================= #
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    insignia.draw()
    glutSwapBuffers()

# ========================= Teclado ========================= #
def keyboard(key, x, y):
    # Pressione C
    if key == b'c' or key == b'C':
        insignia.energize()
        glutPostRedisplay()

# ========================= Inicialização ========================= #
def init():
    glClearColor(0.05, 0.05, 0.08, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)

# ========================= Main ========================= #
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Insignia de Malta")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()