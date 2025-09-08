import pygame, time

pygame.init()

# --- Screen ---
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Player ---
x, y = 100, height - 50
speed = 5
player_width, player_height = 50, 50
score = 0

# --- Enemy ---
enemy_x, enemy_y = 400, height - 50
enemy_width, enemy_height = 50, 50
base_enemy_speed = 5
enemy_velocity = base_enemy_speed
enemy_direction = 1  # 1 = right, -1 = left
bounce_flag = False  # track if we already scored for this bounce

# --- Physics ---
gravity = 1
velocity_y = 0
jump_strength = 15
jump_cooldown = 0.3
last_jump_time = 0

# --- Ground ---
ground_level = height - player_height

running = True
while running:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and y == ground_level:
        if current_time - last_jump_time >= jump_cooldown:
            velocity_y = -jump_strength
            last_jump_time = current_time

    # --- Gravity + Movement ---
    velocity_y += gravity
    y += velocity_y

    # --- Boundary checks for player ---
    if x + player_width > width:
        x = width - player_width
    if x < 0:
        x = 0
    if y > ground_level:
        y = ground_level
        velocity_y = 0

    # --- Collision between player and enemy ---
    if (x + player_width > enemy_x and x < enemy_x + enemy_width) and \
       (y + player_height > enemy_y and y < enemy_y + enemy_height):
        pygame.quit()
        print(score)

    # --- Enemy movement ---
    enemy_velocity = base_enemy_speed + score * 0.4
    enemy_x += enemy_velocity * enemy_direction

    # Bounce and score
    if enemy_x + enemy_width > width:
        enemy_direction = -1
        if not bounce_flag:
            score += 1
            bounce_flag = True
    elif enemy_x < 0:
        enemy_direction = 1
        if not bounce_flag:
            score += 1
            bounce_flag = True
    else:
        bounce_flag = False  # reset flag when enemy is away from edges

    # --- Drawing ---
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, player_width, player_height))
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_width, enemy_height))
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(score)