import pygame
import random
class Snake_Game:
    def __init__(self):
        pygame.init()
        self.width=800
        self.height=800
        self.game=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.run=True
        self.clock=pygame.time.Clock()
        self.score=0
        self.font=pygame.font.Font(None, 50)
        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
        self.display_score_rect=self.display_score.get_rect(center=(80, 50))
        self.countdown=18000000
        self.game_active=False
        self.display_final_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
        self.display_final_score_rect=self.display_final_score.get_rect(center=(400, 400))
        self.display_title=self.font.render("Snake Game", False, (255, 0, 0))
        self.display_title_rect=self.display_title.get_rect(center=(400, 50))
        self.display_space_text=self.font.render("Press Space to play", False, (0, 0, 0))
        self.display_space_text_rect=self.display_space_text.get_rect(center=(400, 700))
        
    def run_game(self):
        self.snake=Snake()
        self.apple=Apple()
        self.apple.spawn_apple()
        while self.run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE and self.game_active==False:
                        self.countdown=1000
                        self.score=0
                        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                        self.snake=Snake()  
                        self.apple=Apple()
                        self.apple.spawn_apple()
                        self.game_active=True

            if self.game_active:
                self.game.fill((0, 255, 0))
                self.snake.create_snake(self.game)
                self.snake.move_snake()
                self.game.blit(self.apple.Apple, self.apple.Apple_rect)
                self.game.blit(self.display_score, self.display_score_rect)
                self.countdown=self.countdown-1
                if self.snake.snake_rect.colliderect(self.apple.Apple_rect):
                    self.score=self.score+1
                    self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                    self.apple.spawn_apple()
                if self.countdown==0:
                    self.game_active=False
            else:
                self.game.fill(((0, 255, 0)))
                self.display_final_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                self.game.blit(self.display_final_score, self.display_final_score_rect)
                self.game.blit(self.display_space_text, self.display_space_text_rect)
                self.game.blit(self.display_title, self.display_title_rect)
            
            self.clock.tick(30) 
            pygame.display.update()

        pygame.quit()

class Snake:
    def __init__(self):
        self.x=400
        self.y=400
        self.width=20
        self.height=100
        self.snake_rect=pygame.Rect(self.x, self.y, self.width, self.height)
        self.angle=0
    def create_snake(self, surface):
        rotated_surface=pygame.Surface((self.width, self.height))  
        rotated_surface.fill((255, 0, 0))  
        rotated_surface=pygame.transform.rotate(rotated_surface, self.angle)
        new_rect=rotated_surface.get_rect(center=self.snake_rect.center)
        surface.blit(rotated_surface, new_rect)
    def move_snake(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.snake_rect.y-=5
            self.angle=0  
        if keys[pygame.K_s] and not keys[pygame.K_d] and not keys[pygame.K_a]:
            self.snake_rect.y+=5
            self.angle=180  
        if keys[pygame.K_a] and not keys[pygame.K_w]:
            self.snake_rect.x-=5
            self.angle=90  
        if keys[pygame.K_d] and not keys[pygame.K_w]:
            self.snake_rect.x+=5
            self.angle=270
       
        if self.snake_rect.y<=0:
            self.snake_rect.y=0
        elif self.snake_rect.y>=700:
            self.snake_rect.y=700
        elif self.snake_rect.x>=740:
            self.snake_rect.x=740
        elif self.snake_rect.x<=40:
            self.snake_rect.x=40

class Apple:
    def __init__(self):
        self.Apple=pygame.image.load("apple.png").convert_alpha()
    def spawn_apple(self):
        self.Apple_rect=self.Apple.get_rect(center=(random.randint(50, 750), random.randint(50, 750)))


        
        
game=Snake_Game()
game.run_game()
       
