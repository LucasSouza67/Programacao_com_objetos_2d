from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import math


# =================== CONFIGURAÇÕES ================== #

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

MIN_RADIUS = 10
MAX_RADIUS = 50

MIN_COORD = -90
MAX_COORD = 90

INITIAL_STARS = 7


# ======================= CLASSE ESTRELA ====================== #
class Star:
    def __init__(self, x, y, radius, color):

        self.x = x
        self.y = y

        self.radius = radius

        self.color = color

        self.vertices = []
        self.indices = []

        self.generate_circle()

    # ===== GERAÇÃO DO CÍRCULO ===== #

    def generate_circle(self, segments=40):

        # vértice central
        self.vertices.append((0, 0))

        # borda do círculo
        for i in range(segments):

            angle = 2 * math.pi * i / segments

            vx = self.radius * math.cos(angle)
            vy = self.radius * math.sin(angle)

            self.vertices.append((vx, vy))

        # triangulação
        for i in range(1, segments):

            self.indices.extend([
                0, i, i + 1
            ])

        self.indices.extend([
            0, segments, 1
        ])

    def draw(self):
        glColor3f(*self.color)
        glBegin(GL_TRIANGLES)
        
        for index in self.indices:
            vx, vy = self.vertices[index]
            glVertex2f(vx + self.x, vy + self.y)
        glEnd()


# ================ CONSTELAÇÃO ================ #
class Constellation:
    def __init__(self):
        self.stars = []
        self.night_mode = False
        self.generate_initial_stars()
        
    # COR ALEATÓRIA
    def random_color(self):

        return (
            random.random(),
            random.random(),
            random.random()
        )
        
    # MODO NOTURNA
    def night_color(self):

        colors = [

            (1, 1, 1),       # branco

            (1, 1, 0.6),     # amarelo claro

            (1, 0.9, 0.5)
        ]

        return random.choice(colors)

    # ============ CRIAÇÃO DAS ESTRELAS ============ #
    def create_star(self):

        x = random.randint(MIN_COORD, MAX_COORD)

        y = random.randint(MIN_COORD, MAX_COORD)
        
        radius = random.randint(MIN_RADIUS, MAX_RADIUS)

        if self.night_mode:
            color = self.night_color()
        else:
            color = self.random_color()

        return Star(x, y, radius, color)

    # =========== GERAÇÃO INICIAL =========== # 

    def generate_initial_stars(self):

        self.stars.clear()

        for _ in range(INITIAL_STARS):

            self.stars.append(
                self.create_star()
            )

    # ADICIONAR ESTRELA
    def add_star(self):
        self.stars.append(
            self.create_star()
        )

    # REMOVER ESTRELA
    def remove_star(self):
        if len(self.stars) > 0:
            index = random.randint(
                0,
                len(self.stars) - 1
            )
            self.stars.pop(index)

    # RESETAR
    def reset(self):
        self.generate_initial_stars()

    # MODO NOTURNO
    def toggle_night_mode(self):
        self.night_mode = not self.night_mode

        for star in self.stars:
            if self.night_mode:
                star.color = self.night_color()
            else:
                star.color = self.random_color()

    # CONEXÕES
    def draw_connections(self):

        glLineWidth(1.5)

        if self.night_mode:
            glColor3f(0.6, 0.6, 1)
        else:
            glColor3f(1, 1, 1)

        glBegin(GL_LINES)

        for i in range(len(self.stars) - 1):

            s1 = self.stars[i]
            s2 = self.stars[i + 1]

            glVertex2f(s1.x, s1.y)
            glVertex2f(s2.x, s2.y)

        glEnd()

    # DESENHAR CONSTELAÇÃO
    def draw(self):
        self.draw_connections()

        for star in self.stars:
            star.draw()


constellation = Constellation()

# ========================= DISPLAY ========================= #
def display():
    if constellation.night_mode:
        glClearColor(0, 0, 0, 1)

    else:
        glClearColor(0.08, 0.08, 0.12, 1)

    glClear(GL_COLOR_BUFFER_BIT)
    constellation.draw()
    glutSwapBuffers()

# ============ TECLADO ============ #
def keyboard(key, x, y):
    # adicionar estrela
    if key == b'n':
        constellation.add_star()
    # remover estrela
    elif key == b'x':
        constellation.remove_star()
    # resetar
    elif key == b'r':
        constellation.reset()
    # modo noturno
    elif key == b't':
        constellation.toggle_night_mode()
    glutPostRedisplay()
    
# ========================= INICIALIZAÇÃO ========================= #
def init():

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(-100, 100, -100, 100)

# ========================= MAIN ========================= #
def main():

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    )

    glutCreateWindow(
        b"Constelacao dos Guardioes"
    )

    init()

    glutDisplayFunc(display)

    glutKeyboardFunc(keyboard)

    glutMainLoop()


if __name__ == "__main__":
    main()