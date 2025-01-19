# KEX

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

camera_pos = [0.0, 0.0, 0.0]
player_pos = [0, 0, 0]
camera_rot = [0.0, 0.0]

start_position = [0.0, 0.0, 0.0]


def generate_cube_vertices(pos):
    x, y, z = pos
    return [
        (x + 1, y - 1, z - 1),
        (x + 1, y + 1, z - 1),
        (x - 1, y + 1, z - 1),
        (x - 1, y - 1, z - 1),
        (x + 1, y - 1, z + 1),
        (x + 1, y + 1, z + 1),
        (x - 1, y - 1, z + 1),
        (x - 1, y + 1, z + 1),
    ]

vertices = generate_cube_vertices(player_pos)

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (0, 5),
    (2, 6),
    (3, 7),
]


# Function to draw the cube
def draw_cube(vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_multiple_cubes(cubes):
    for cube_vertices in cubes:
        draw_cube(cube_vertices)


pygame.init()
running = True
display = (1920, 1080)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(90, (display[0] / display[1]), 0.2, 50.0)

p_start_x = 0
n_start_x = 0
n_start_y = 0
p_start_y = 0

cubes = [
    vertices,
]

rotate = True

position = [0.0, 0.0, 0.0]

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed. Exiting...")
                running = False
            elif event.key == pygame.K_z:
                cubes = [[(x, y, z + 0.1) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_y:
                cubes = [[(x, y + 0.1, z) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_n:
                cubes = [[(x + 0.1, y, z) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_c:
                cubes = [[(x, y, z - 0.1) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_v:
                cubes = [[(x, y - 0.1, z) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_b:
                cubes = [[(x - 0.1, y, z) for (x, y, z) in cube] for cube in cubes]
            elif event.key == pygame.K_RIGHT:
                n_start_x += 2
                cubes.append([(x + n_start_x, y, z) for (x, y, z) in vertices])
            elif event.key == pygame.K_LEFT:
                p_start_x += 2
                ln_start = 0 - p_start_x
                cubes.append([(x + ln_start, y, z) for (x, y, z)in vertices])
            elif event.key == pygame.K_UP:
                p_start_y += 2
                cubes.append([(x, y + p_start_y, z) for (x, y, z) in vertices])
            elif event.key == pygame.K_DOWN:
                p_start_y -= 2
                cubes.append([(x, y + p_start_y, z) for (x, y, z) in vertices])
            elif event.key == pygame.K_w:
                player_pos[2] += 1
                camera_pos[2] += 0.01
            elif event.key == pygame.K_s:
                player_pos[2] -= 1
                camera_pos[2] -= 0.01
            elif event.key == pygame.K_a:
                player_pos[0] += 1
                camera_pos[0] += 0.01
            elif event.key == pygame.K_d:
                player_pos[2] -= 1
                camera_pos[0] -= 0.01
            elif event.key == pygame.K_r:
                glRotatef(1, 3, 1, 1)

    # Clear the screen and redraw the cubes with rotation
    glTranslatef(camera_pos[0], camera_pos[1], camera_pos[2])
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    print(player_pos)

    draw_multiple_cubes(cubes)  # Draw all cubes
    pygame.display.flip()
    clock.tick(60)
