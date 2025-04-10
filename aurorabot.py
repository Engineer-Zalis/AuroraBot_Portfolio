import pygame
import sys

# Inizializza PyGame
pygame.init()

# Colori
MARS_RED = (138, 54, 15)
ROBOT_COLOR = (255, 255, 255)
OBSTACLE_COLOR = (80, 20, 20)

# Dimensioni finestra e robot
WIDTH, HEIGHT = 800, 600
ROBOT_SIZE = 40
SPEED = 5

# Crea finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AuroraBot – Missione Marziana")

# Posizione iniziale robot
robot_x, robot_y = WIDTH // 2, HEIGHT // 2

# Lista di ostacoli (posizioni x, y, larghezza, altezza)
obstacles = [
    pygame.Rect(300, 150, 100, 100),
    pygame.Rect(500, 350, 120, 100),
    pygame.Rect(150, 450, 60, 60),
]

clock = pygame.time.Clock()

# LOOP PRINCIPALE
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tasti premuti
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= SPEED
    if keys[pygame.K_RIGHT]:
        robot_x += SPEED
    if keys[pygame.K_UP]:
        robot_y -= SPEED
    if keys[pygame.K_DOWN]:
        robot_y += SPEED

    # Crea rettangolo robot
    robot = pygame.Rect(robot_x, robot_y, ROBOT_SIZE, ROBOT_SIZE)

    # Collisione con ostacoli (banale per ora)
    for obstacle in obstacles:
        if robot.colliderect(obstacle):
            print("💥 Collisione con ostacolo!")
            # Riporta indietro il robot
            if keys[pygame.K_LEFT]:
                robot_x += SPEED
            if keys[pygame.K_RIGHT]:
                robot_x -= SPEED
            if keys[pygame.K_UP]:
                robot_y += SPEED
            if keys[pygame.K_DOWN]:
                robot_y -= SPEED

    # Disegna sfondo marziano
    screen.fill(MARS_RED)

    # Disegna ostacoli
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    # Disegna il robot
    pygame.draw.rect(screen, ROBOT_COLOR, robot)

    pygame.display.flip()
    clock.tick(60)


