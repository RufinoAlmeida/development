import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo do Dinossauro")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)

# Configurações do jogo
GROUND_HEIGHT = 50
GRAVITY = 0.7
JUMP_STRENGTH = -13
GAME_SPEED = 5

class Dinosaur:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT - GROUND_HEIGHT - 60
        self.width = 40
        self.height = 60
        self.vel_y = 0
        self.jumping = False
        self.ducking = False
        
    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_STRENGTH
            self.jumping = True
    
    def duck(self):
        self.ducking = True
        self.height = 30
    
    def stop_duck(self):
        self.ducking = False
        self.height = 60
        if not self.jumping:
            self.y = SCREEN_HEIGHT - GROUND_HEIGHT - 60
    
    def update(self):
        # Aplicar gravidade
        if self.jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            
            # Verificar se tocou o chão
            if self.y >= SCREEN_HEIGHT - GROUND_HEIGHT - self.height:
                self.y = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
                self.vel_y = 0
                self.jumping = False
    
    def draw(self, screen):
        # Desenhar dinossauro (retângulo simples)
        color = GREEN if not self.ducking else (0, 200, 0)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        
        # Desenhar olho
        pygame.draw.circle(screen, WHITE, (self.x + 10, self.y + 15), 5)
        pygame.draw.circle(screen, BLACK, (self.x + 12, self.y + 15), 3)

class Obstacle:
    def __init__(self, x):
        self.x = x
        self.width = 20
        self.height = random.randint(40, 80)
        self.y = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
        
    def update(self):
        self.x -= GAME_SPEED
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        return self.x + self.width < 0

class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 30
        
    def update(self):
        self.x -= GAME_SPEED // 2
    
    def draw(self, screen):
        # Desenhar nuvem simples
        pygame.draw.ellipse(screen, GRAY, (self.x, self.y, 20, 20))
        pygame.draw.ellipse(screen, GRAY, (self.x + 15, self.y, 25, 25))
        pygame.draw.ellipse(screen, GRAY, (self.x + 30, self.y, 20, 20))
    
    def is_off_screen(self):
        return self.x + self.width < 0

class Game:
    def __init__(self):
        self.dino = Dinosaur()
        self.obstacles = []
        self.clouds = []
        self.score = 0
        self.game_over = False
        self.game_started = False
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Timer para spawnar obstáculos
        self.obstacle_timer = 0
        self.cloud_timer = 0
        
    def spawn_obstacle(self):
        if len(self.obstacles) == 0 or self.obstacles[-1].x < SCREEN_WIDTH - 200:
            self.obstacles.append(Obstacle(SCREEN_WIDTH))
    
    def spawn_cloud(self):
        if random.randint(1, 100) == 1:
            self.clouds.append(Cloud(SCREEN_WIDTH, random.randint(50, 150)))
    
    def check_collision(self):
        dino_rect = pygame.Rect(self.dino.x, self.dino.y, self.dino.width, self.dino.height)
        
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
            if dino_rect.colliderect(obstacle_rect):
                return True
        return False
    
    def update(self):
        if not self.game_over and self.game_started:
            self.dino.update()
            
            # Atualizar obstáculos
            for obstacle in self.obstacles[:]:
                obstacle.update()
                if obstacle.is_off_screen():
                    self.obstacles.remove(obstacle)
                    self.score += 1
            
            # Atualizar nuvens
            for cloud in self.clouds[:]:
                cloud.update()
                if cloud.is_off_screen():
                    self.clouds.remove(cloud)
            
            # Spawnar novos elementos
            self.spawn_obstacle()
            self.spawn_cloud()
            
            # Verificar colisão
            if self.check_collision():
                self.game_over = True
    
    def draw(self, screen):
        screen.fill(WHITE)
        
        # Desenhar chão
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        
        # Desenhar nuvens
        for cloud in self.clouds:
            cloud.draw(screen)
        
        # Desenhar dinossauro
        self.dino.draw(screen)
        
        # Desenhar obstáculos
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        # Desenhar pontuação
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Desenhar mensagens
        if not self.game_started:
            start_text = self.font.render("Pressione ESPAÇO para começar", True, BLACK)
            text_rect = start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(start_text, text_rect)
            
            controls_text = self.small_font.render("ESPAÇO: Pular | SETA BAIXO: Abaixar", True, BLACK)
            controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            screen.blit(controls_text, controls_rect)
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(game_over_text, text_rect)
            
            restart_text = self.small_font.render("Pressione R para reiniciar", True, BLACK)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            screen.blit(restart_text, restart_rect)
    
    def restart(self):
        self.dino = Dinosaur()
        self.obstacles = []
        self.clouds = []
        self.score = 0
        self.game_over = False
        self.game_started = False

def main():
    clock = pygame.time.Clock()
    game = Game()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game.game_started and not game.game_over:
                        game.game_started = True
                    elif not game.game_over:
                        game.dino.jump()
                
                if event.key == pygame.K_DOWN:
                    if game.game_started and not game.game_over:
                        game.dino.duck()
                
                if event.key == pygame.K_r and game.game_over:
                    game.restart()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    game.dino.stop_duck()
        
        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()