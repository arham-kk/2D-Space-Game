import pygame, random

# Initialize Pygame
pygame.init()

# Define a list to hold enemy positions & projectile positions
enemies = []
projectiles = []

# Spawn a new enemy every 1.5 seconds
enemy_spawn_timer = 0

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Shooting Game")

# Load game assets
player_image = pygame.transform.scale(pygame.image.load("assets/player.png"), (50, 50))
enemy_image = pygame.transform.scale(pygame.image.load("assets/enemy.png"), (50, 50))
projectile_image = pygame.transform.scale(pygame.image.load("assets/projectile.png"), (50, 50))
explosion_image = pygame.transform.scale(pygame.image.load("assets/blast.png"), (50, 50))
bullet_sound = pygame.mixer.Sound("assets/bullet.wav")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
gameover_image = pygame.transform.scale(pygame.image.load("assets/gameover.png"), (400, 250))
gameover_sound = pygame.mixer.Sound("assets/gameover.mp3")

# Set the initial position of the player
player_x = 400
player_y = 500

# Set up the font for the score
score_font = pygame.font.Font(None, 36)
# Initialize the score
score = 0

# Create the game loop
clock = pygame.time.Clock()
is_running = True
is_paused = False
is_game_over = False
while is_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new projectile and play the bullet sound
                projectiles.append([player_x + player_image.get_width() / 2 - projectile_image.get_width() / 2, player_y])
                bullet_sound.play()
            if event.key == pygame.K_ESCAPE:
                is_paused = not is_paused
                
    # Handle pause menu events
    if is_paused:
        # Render pause menu
        pause_font = pygame.font.SysFont("Arial", 50)
        pause_text = pause_font.render("Paused", True, (255,255,255))
        pause_rect = pause_text.get_rect(center=(window_width/2, window_height/2 - 50))
        window.blit(pause_text, pause_rect)

        resume_text = score_font.render("Press SPACE to resume", True, (255,255,255))
        resume_rect = resume_text.get_rect(center=(window_width/2, window_height/2))
        window.blit(resume_text, resume_rect)

        exit_text = score_font.render("Press ESC to exit", True, (255,255,255))
        exit_rect = exit_text.get_rect(center=(window_width/2, window_height/2 + 50))
        window.blit(exit_text, exit_rect)

        pygame.display.update()

        # Wait for user to resume or exit
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_paused = False
                    if event.key == pygame.K_ESCAPE:
                        is_running = False
                        is_paused = False
    elif not is_game_over:
        # Update game state
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 5
        if keys[pygame.K_RIGHT]:
            player_x += 5
        if keys[pygame.K_UP]:
            player_y -= 5
        if keys[pygame.K_DOWN]:
            player_y += 5

        # Spawn a new enemy every 1.5 seconds
        enemy_spawn_timer += clock.get_time()
        if enemy_spawn_timer >= 1500:
            enemies.append([random.randint(0, window_width - enemy_image.get_width()), -enemy_image.get_height()])
            enemy_spawn_timer = 0

        # Move enemies down the screen and remove them if they go off the bottom
        for enemy in enemies:
            enemy[1] += 3
            if enemy[1] > window_height:
                enemies.remove(enemy)

        # Move projectiles up the screen and remove them if they go off the top
        for projectile in projectiles:
            projectile[1] -= 5
            if projectile[1] < -projectile_image.get_height():
                projectiles.remove(projectile)

    def check_collision(proj_x, proj_y, proj_w, proj_h, enemy_x, enemy_y, enemy_w, enemy_h):
        proj_rect = pygame.Rect(proj_x, proj_y, proj_w, proj_h)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)
        return proj_rect.colliderect(enemy_rect)

    # Render game objects
    window.fill((0, 0, 0))
    window.blit(player_image, (player_x, player_y))

    # Move projectiles up the screen and remove them if they go off the top
    for projectile in projectiles:
        projectile[1] -= 5
        if projectile[1] < -projectile_image.get_height():
            projectiles.remove(projectile)
        else:
            # Check for collision with enemies
            for enemy in enemies:
                if check_collision(projectile[0], projectile[1], projectile_image.get_width(), projectile_image.get_height(), enemy[0], enemy[1], enemy_image.get_width(), enemy_image.get_height()):
                    projectiles.remove(projectile)
                    enemies.remove(enemy)
                    explosion_rect = explosion_image.get_rect(center=(enemy[0] + enemy_image.get_width() / 2, enemy[1] + enemy_image.get_height() / 2))
                    window.blit(explosion_image, explosion_rect)
                    explosion_sound.play()
                    score += 10
        window.blit(projectile_image, (projectile[0], projectile[1]))

    for enemy in enemies:
        window.blit(enemy_image, (enemy[0], enemy[1]))
        if enemy[1] > window_height - enemy_image.get_height() - 10:
        # Enemy reached the bottom, game over
            is_running = False

    # Render score
    score_font = pygame.font.SysFont("Arial", 25)
    score_text = score_font.render(f"Score: {score}", True, (255,255,255))
    window.blit(score_text, (10, 10))

    pygame.display.update()

    # Limit frame rate
    clock.tick(60)

gameover_rect = gameover_image.get_rect(center=(window_width/2, window_height/2))
window.blit(gameover_image, gameover_rect)
pygame.display.update()
gameover_sound.play()

pygame.time.wait(5000)
pygame.quit()
