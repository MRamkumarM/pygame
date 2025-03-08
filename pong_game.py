import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
FPS = 60
wn = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Creating the panel
p_x1, p_x2 = 0, 780
p_y1, p_y2 = 300, 300
panel1 = pygame.Rect(p_x1, p_y1, 20, 200)
panel2 = pygame.Rect(p_x2, p_y2, 20, 200)

# Creating the ball
ball = pygame.Rect(400, 400, 20, 20)  # ball size: 20x20
ball_velocity_x = 5  # Ball horizontal speed
ball_velocity_y = 5  # Ball vertical speed

# Ball bounce variables
bx, by = 400, 400
velocity = 5  # Adjust ball speed

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        p_y2 -= 5
    if key[pygame.K_DOWN]:
        p_y2 += 5
    if key[pygame.K_w]:
        p_y1 -= 5
    if key[pygame.K_s]:
        p_y1 += 5

    # Keep paddles within screen bounds
    if p_y1 < 0:
        p_y1 = 0
    if p_y2 < 0:
        p_y2 = 0
    if p_y1 > HEIGHT - 200:
        p_y1 = HEIGHT - 200
    if p_y2 > HEIGHT - 200:
        p_y2 = HEIGHT - 200

    # Update the panel (paddle) positions
    panel1.y = p_y1
    panel2.y = p_y2

    # Update ball position
    bx += ball_velocity_x
    by += ball_velocity_y

    # Ball collision with the top and bottom walls
    if by - 10 < 0 or by + 10 > HEIGHT:
        ball_velocity_y = -ball_velocity_y

    # Ball collision with the left and right walls (scoring)
    if bx - 10 < 0 or bx + 10 > WIDTH:
        bx, by = 400, 400  # Reset the ball to the center

    # Ball collision with paddles
    if panel1.colliderect(pygame.Rect(bx - 10, by - 10, 20, 20)) or panel2.colliderect(pygame.Rect(bx - 10, by - 10, 20, 20)):
        ball_velocity_x = -ball_velocity_x

    wn.fill((0, 0, 0))  # Clear screen with black background
    pygame.draw.rect(wn, (255, 255, 255), panel1)  # Draw left paddle
    pygame.draw.rect(wn, (255, 255, 255), panel2)  # Draw right paddle
    pygame.draw.circle(wn, (255, 255, 255), (bx, by), 10)  # Draw ball

    pygame.display.update()
    clock.tick(FPS)
