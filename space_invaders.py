import pygame
from pygame import key
import random 

class Space_Invaders:
    def __init__(self):
        pygame.init()
        self.width=800
        self.height=800
        self.game=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.space=pygame.image.load("Space.png").convert()
        self.spaceship=pygame.image.load("spaceship.png").convert_alpha()
        self.spaceship_rect=self.spaceship.get_rect(center=(400, 700))
        self.font=pygame.font.Font(None, 50)
        self.run=True
        self.clock=pygame.time.Clock()
        self.game_active=False
        self.play_text=self.font.render("Press Space to play", False, 50)
        self.play_text_rect=self.play_text.get_rect(center=(400, 700))
        self.spaceship_standing=pygame.image.load("spaceship.png").convert_alpha()
        self.spaceship_rect_standing=self.spaceship_standing.get_rect(center=(400, 400))
        self.spaceinvaders_text=self.font.render("Space Invaders", False, 100)
        self.spaceinvaders_text_rect=self.spaceinvaders_text.get_rect(center=(400, 100))
        self.rock=pygame.image.load("rock.png").convert_alpha()
        self.rock_rect1=self.rock.get_rect(center=(100, -50))
        self.rock_rect2=self.rock.get_rect(center=(300, -50))
        self.rock_rect3=self.rock.get_rect(center=(500, -50))
        self.rock_rect4=self.rock.get_rect(center=(700, -50))
        self.score=0
        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
        self.display_score_rect=self.display_score.get_rect(center=(80, 50))
        self.display_finalscore=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
        self.display_finalscore_rect=self.display_finalscore.get_rect(center=(400, 600))
        self.laser_width=5
        self.laser_height=15
        self.laser_speed=5
        self.rock1_speed=random.randint(3, 10)
        self.rock2_speed=random.randint(3, 10)
        self.rock3_speed=random.randint(3, 10)
        self.rock4_speed=random.randint(3, 10)
        self.lasers=[]
        self.enemy=pygame.image.load("enemy.png").convert_alpha()
        self.enemy=pygame.transform.flip(self.enemy, False, True)
        self.enemy_rect1=self.enemy.get_rect(center=(random.randint(50, 750), random.randint(-500, -50)))
        self.enemy_rect2=self.enemy.get_rect(center=(random.randint(50, 750), random.randint(-500, -50)))
        self.enemy_rect3=self.enemy.get_rect(center=(random.randint(50, 750), random.randint(-500, -50)))
        self.enemy_speed1=1
        self.enemy_speed2=1
        self.enemy_speed3=1
        pygame.mixer.init()
        self.laser_sound=pygame.mixer.Sound("lasersound.mp3")
        self.coll_sound=pygame.mixer.Sound("collsound.mp3")
        self.lives=3
        self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
        self.lives_text_rect=self.lives_text.get_rect(center=(80, 110))
        self.stopwatch=0
        self.laser_speed2=2
        self.lasers2=[]
        self.enemy_shooter_time=0
    def play_lasersound(self):
        self.laser_sound.play()
    
    def play_collsound(self):
        self.coll_sound.play()
        
    
    def reset_game(self):
        if not self.game_active:
            self.game_active=True
            self.spaceinvaders_text_rect=self.spaceinvaders_text.get_rect(center=(400, 100))
            self.rock_rect1=self.rock.get_rect(center=(random.randint(50, 150), -50))
            self.rock_rect2=self.rock.get_rect(center=(random.randint(150, 300), -50))
            self.rock_rect3=self.rock.get_rect(center=(random.randint(300, 500), -50))
            self.rock_rect4=self.rock.get_rect(center=(random.randint(500, 750), -50))
            self.score=0
            self.lives=3
            self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
            self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
            self.lasers2.clear() 

            self.rock1_speed=random.randint(3, 10)
            self.rock2_speed=random.randint(3, 10)
            self.rock3_speed=random.randint(3, 10)
            self.rock4_speed=random.randint(3, 10)
            self.enemy_rect1.y=random.randint(-500, -50)
            self.enemy_rect1.x=random.randint(50, 750)
            self.enemy_rect2.y=random.randint(-500, -50)
            self.enemy_rect2.x=random.randint(50, 750)
            self.enemy_rect3.y=random.randint(-500, -50)
            self.enemy_rect3.x=random.randint(50, 750)
            self.enemy_speed1=1
            self.enemy_speed2=1
            self.enemy_speed3=1
            

       

    def run_game(self):
        while self.run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.reset_game()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        laser=pygame.Rect(self.spaceship_rect.centerx, self.spaceship_rect.top, self.laser_width, self.laser_height)
                        self.lasers.append(laser)
                        self.play_lasersound()


                self.keys=pygame.key.get_pressed()
                if self.keys[pygame.K_a]:
                    self.spaceship_rect.x=self.spaceship_rect.x-15
                elif self.keys[pygame.K_d]:
                    self.spaceship_rect.x=self.spaceship_rect.x+15
                if self.spaceship_rect.right>=800:
                    self.spaceship_rect.right=800
                elif self.spaceship_rect.left<=0:
                    self.spaceship_rect.left=0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.game_active=True
            if self.game_active:
                self.game.blit(self.space, (0, 0))
                self.game.blit(self.spaceship, self.spaceship_rect)
                self.game.blit(self.rock, self.rock_rect1)
                self.game.blit(self.rock, self.rock_rect2)
                self.game.blit(self.rock, self.rock_rect3)
                self.game.blit(self.rock, self.rock_rect4)
                self.game.blit(self.display_score, self.display_score_rect)
                self.game.blit(self.enemy, self.enemy_rect1)
                self.game.blit(self.enemy, self.enemy_rect2)
                self.game.blit(self.enemy, self.enemy_rect3)
                self.game.blit(self.lives_text, self.lives_text_rect)
                self.rock_rect1.y=self.rock_rect1.y+self.rock1_speed
                self.rock_rect2.y=self.rock_rect2.y+self.rock2_speed
                self.rock_rect3.y=self.rock_rect3.y+self.rock3_speed
                self.rock_rect4.y=self.rock_rect4.y+self.rock4_speed

                self.enemy_rect1.y=self.enemy_rect1.y+self.enemy_speed1
                self.enemy_rect2.y=self.enemy_rect2.y+self.enemy_speed2
                self.enemy_rect3.y=self.enemy_rect3.y+self.enemy_speed3
                if self.enemy_rect1.y>800:
                    self.enemy_rect1.y=random.randint(-500, -50)
                    self.enemy_rect1.x=random.randint(50, 750)
                elif self.enemy_rect2.y>800:
                    self.enemy_rect2.y=random.randint(-500, -50)
                    self.enemy_rect2.x=random.randint(50, 750)
                elif self.enemy_rect3.y>800:
                    self.enemy_rect3.y=random.randint(-500, -50)
                    self.enemy_rect3.x=random.randint(50, 750)
                
                for laser in self.lasers:
                    laser.y=laser.y-self.laser_speed
                    if laser.bottom<100:
                        self.lasers.remove(laser)
                            
                            
                if self.rock_rect1.y>800:
                    self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                    self.rock_rect1.y=-50
                    self.rock_rect1.x=random.randint(50, 150)
                    self.rock1_speed=random.randint(3, 10)
                if self.rock_rect2.y>800:
                    self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                    self.rock_rect2.y=-50
                    self.rock_rect2.x=random.randint(150, 300)
                    self.rock2_speed=random.randint(3, 10)
                if self.rock_rect3.y>800:
                    self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                    self.rock_rect3.y=-50
                    self.rock_rect3.x=random.randint(300, 500)
                    self.rock3_speed=random.randint(3, 10)
                if self.rock_rect4.y>800:
                    self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                    self.rock_rect4.y=-50
                    self.rock_rect4.x=random.randint(500, 750)
                    self.rock4_speed=random.randint(3, 10)
                
                if self.spaceship_rect.colliderect(self.rock_rect1):
                    self.play_collsound()
                    self.lives=self.lives-1
                    self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                    self.rock_rect1.y=-50
                    self.rock_rect1.x=random.randint(500, 750)
                    self.rock1_speed=random.randint(3, 10)
                elif self.spaceship_rect.colliderect(self.rock_rect2):
                    self.play_collsound()
                    self.lives=self.lives-1
                    self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                    self.rock_rect2.y=-50
                    self.rock_rect2.x=random.randint(500, 750)
                    self.rock2_speed=random.randint(3, 10)
                elif self.spaceship_rect.colliderect(self.rock_rect3):
                    self.play_collsound()
                    self.lives=self.lives-1
                    self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                    self.rock_rect3.y=-50
                    self.rock_rect3.x=random.randint(500, 750)
                    self.rock3_speed=random.randint(3, 10)
                elif self.spaceship_rect.colliderect(self.rock_rect4):
                    self.play_collsound()
                    self.lives=self.lives-1
                    self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                    self.rock_rect4.y=-50
                    self.rock_rect4.x=random.randint(500, 750)
                    self.rock4_speed=random.randint(3, 10)
                
                
                
               
                for enemy_rect in [self.enemy_rect1, self.enemy_rect2, self.enemy_rect3]:
                    if enemy_rect.y>50:
                        self.enemy_shooter_time=self.enemy_shooter_time+1
                        if self.enemy_shooter_time>=50:
                            laser2 = pygame.Rect(enemy_rect.centerx, enemy_rect.bottom, self.laser_width, self.laser_height)
                            self.lasers2.append(laser2)
                            self.enemy_shooter_time=0
                        

               
                for laser2 in self.lasers2[:]:  
                    laser2.y += self.laser_speed2
                    if laser2.bottom>710:  
                        self.lasers2.remove(laser2)
                for laser2 in self.lasers2:
                    pygame.draw.rect(self.game, (255, 0, 0), laser2)


                

                                
                self.stopwatch=self.stopwatch+1
                
                if self.stopwatch%5000==0:
                    self.lives=self.lives+1
                    self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                    
                if self.lives==0:
                    self.game_active=False
                

                
           
               
                for laser in self.lasers:
                    pygame.draw.rect(self.game, (0, 0, 255), laser)

                for laser in self.lasers:
                    if self.rock_rect1.colliderect(laser):
                        self.score=self.score+1
                        self.rock_rect1.y=-50
                        self.rock_rect1.x=random.randint(50, 150)
                        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                        self.lasers.remove(laser)
                        self.rock1_speed=random.randint(3, 10)
                    elif self.rock_rect2.colliderect(laser):
                        self.score=self.score+1
                        self.rock_rect2.y=-50
                        self.rock_rect2.x=random.randint(150, 300)
                        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                        self.lasers.remove(laser)
                        self.rock2_speed=random.randint(3, 10)
                    elif self.rock_rect3.colliderect(laser):
                        self.score=self.score+1
                        self.rock_rect3.y=-50
                        self.rock_rect3.x=random.randint(300, 500)
                        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                        self.lasers.remove(laser)
                        self.rock3_speed=random.randint(3, 10)
                    elif self.rock_rect4.colliderect(laser):
                        self.score=self.score+1
                        self.rock_rect4.y=-50
                        self.rock_rect4.x=random.randint(500, 700)
                        self.display_score=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                        self.lasers.remove(laser)
                        self.rock4_speed=random.randint(3, 10)
                    
                    if self.enemy_rect1.colliderect(laser):
                        self.score=self.score+5
                        self.enemy_rect1.y=random.randint(-500, -50)
                        self.enemy_rect1.x=random.randint(50, 750)
                        self.enemy_speed1=1
                        self.lasers2.clear() 
                        self.lasers.remove(laser)
                    elif self.enemy_rect2.colliderect(laser):
                        self.score=self.score+5
                        self.enemy_rect2.y=random.randint(-500, -50)
                        self.enemy_rect2.x=random.randint(50, 750)
                        self.enemy_speed2=1
                        self.lasers2.clear() 
                        self.lasers.remove(laser)
                    elif self.enemy_rect3.colliderect(laser):
                        self.score=self.score+5
                        self.enemy_rect3.y=random.randint(-500, -50)
                        self.enemy_rect3.x=random.randint(50, 750)
                        self.enemy_speed3=1
                        self.lasers2.clear() 
                        self.lasers.remove(laser)
                for laser2 in self.lasers2:
                    if self.spaceship_rect.colliderect(laser2):
                        self.lives=self.lives-1
                        self.lives_text=self.font.render(f"Lives: {self.lives}", False, (255, 0, 0))
                        self.lasers2.remove(laser2)




                    
            


                    



                


            

            else:
                self.game.fill((100,149,237))
                self.game.blit(self.spaceinvaders_text, self.spaceinvaders_text_rect)
                self.game.blit(self.spaceship_standing, self.spaceship_rect_standing)
                self.game.blit(self.play_text, self.play_text_rect)
                self.display_finalscore=self.font.render(f"Score: {self.score}", False, (255, 0, 0))
                self.game.blit(self.display_finalscore, self.display_finalscore_rect)
            pygame.display.update() 
            self.clock.tick(60)
        pygame.quit()

game_open=Space_Invaders()
game_open.run_game()
