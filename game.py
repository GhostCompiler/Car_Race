import pygame
import random

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
CAR_WIDTH, CAR_HEIGHT = 80, 160
ROAD_WIDTH = 400
ROAD_LEFT = (SCREEN_WIDTH - ROAD_WIDTH) // 2
ROAD_RIGHT = ROAD_LEFT + ROAD_WIDTH
WHITE, RED, BLACK = (255, 255, 255), (255, 0, 0), (0, 0, 0)
FPS = 60

class Car:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
        self.y = SCREEN_HEIGHT - CAR_HEIGHT - 20
        self.speed_x = 0
        self.image = pygame.transform.scale(pygame.image.load('static/assets/car_nfs.png'), (CAR_WIDTH, CAR_HEIGHT))
        self.rect = pygame.Rect(self.x, self.y, CAR_WIDTH, CAR_HEIGHT)

    def move(self, direction):
        if direction == "left" and self.x > ROAD_LEFT:
            self.speed_x = -5
        elif direction == "right" and self.x < ROAD_RIGHT - CAR_WIDTH:
            self.speed_x = 5
        else:
            self.speed_x = 0

    def update(self):
        self.x += self.speed_x
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Road:
    def __init__(self):
        self.y = 0
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load('static/assets/road_nfs.jpg'), (ROAD_WIDTH, SCREEN_HEIGHT))

    def update(self):
        self.y = (self.y + self.speed) % SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, (ROAD_LEFT, self.y))
        screen.blit(self.image, (ROAD_LEFT, self.y - SCREEN_HEIGHT))

class Hurdle:
    def __init__(self):
        self.width, self.height = 50, 50
        self.x = random.randint(ROAD_LEFT, ROAD_RIGHT - self.width)
        self.y = -self.height
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Car Racing Game")
        self.clock = pygame.time.Clock()

        self.car = Car()
        self.road = Road()
        self.hurdles = []
        self.running = True
        self.score = 0

        self.play_background_music()

    def spawn_hurdle(self):
        if len(self.hurdles) < 3:
            self.hurdles.append(Hurdle())

    def check_collision(self):
        for hurdle in self.hurdles:
            if self.car.rect.colliderect(hurdle.rect):
                self.running = False  # Game Over

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def show_game_over(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 72)
        text = font.render("GAME OVER", True, RED)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        quit()

    def play_background_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load('static/assets/background_music.wav')
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.car.move("left")
        elif keys[pygame.K_RIGHT]:
            self.car.move("right")
        else:
            self.car.move(None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.road.update()
        self.car.update()
        self.spawn_hurdle()
        for hurdle in self.hurdles:
            hurdle.update()
            if hurdle.y > SCREEN_HEIGHT:
                self.hurdles.remove(hurdle)

        self.check_collision()
        self.score += 1

    def draw(self):
        self.screen.fill(BLACK)
        self.road.draw(self.screen)
        for hurdle in self.hurdles:
            hurdle.draw(self.screen)
        self.car.draw(self.screen)
        self.display_score()
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.show_game_over()

# Run the game
if __name__ == "__main__":
    Game().run()
