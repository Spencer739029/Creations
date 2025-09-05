import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen.fill((0, 0, 0))
pygame.display.flip()
counter = 0
font = pygame.font.Font(None, 36)  
start_time = time.time()
timer_duration = 15  # 15 seconds

def draw_circle():
    x = random.randint(30, 1170)
    y = random.randint(30, 770)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)
    return pygame.Rect(x - 30, y - 30, 60, 60)

running = True
circle_rect = draw_circle()

while running:
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 0, 0), circle_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if circle_rect.collidepoint(event.pos):
                counter += 1
                circle_rect = draw_circle()
            else:
                counter -= 5
                print("Circle missed!")

    # --- Check score loss ---
    if counter < 0:
        screen.fill((0, 0, 0))
        font_big = pygame.font.Font(None, 150)
        text = font_big.render("GAME OVER", True, (255, 0, 0))  # red
        text_rect = text.get_rect(center=(600, 400))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        counter = 0

    # --- Timer countdown ---
    elapsed = time.time() - start_time
    remaining = max(0, int(timer_duration - elapsed))
    if remaining <= 0:
        screen.fill((0, 0, 0))
        font_big = pygame.font.Font(None, 150)
        text = font_big.render("TIME UP!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(600, 400))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # --- Draw score ---
    text = font.render(f"Score: {counter}", True, (255, 255, 255))  # white
    text_rect = text.get_rect(topright=(1180, 10))
    screen.blit(text, text_rect)

    # --- Draw timer ---
    timer_text = font.render(f"Time: {remaining}", True, (255, 255, 255))
    timer_rect = timer_text.get_rect(topleft=(10, 10))
    screen.blit(timer_text, timer_rect)

    pygame.display.flip()

pygame.quit()
print(f"Final Score = {counter}")
