import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	'''Class for controlling ship's projectiles '''
	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.setts=ai_game.setts
		self.color=self.setts.bullet_color
		self.rect=pygame.Rect(
			0,0,self.setts.bullet_width,self.setts.bullet_height)
		self.rect.midtop=ai_game.ship.rect.midtop
		self.y=float(self.rect.y)
	def update(self): 
		self.y-=self.setts.bullet_speed
		self.rect.y=self.y
	def draw_bullet(self):
		#pygame.draw.rect(self.screen,self.color,self.rect)
		self.screen.fill(self.color,self.rect)
