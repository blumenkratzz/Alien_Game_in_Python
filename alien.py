import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.stats=ai_game.stats
		self.check_level()
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
		self.setts=ai_game.setts
	def update(self):
		self.x+=(self.setts.alien_speed*
			self.setts.fleet_direction)
		self.rect.x=self.x
	def check_edges(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right or self.rect.left<=0:
			return True
	def check_level(self):
		if self.stats.level==1:
			self.image=pygame.image.load('images/alien_st.bmp')
		if self.stats.level==2:
			self.image=pygame.image.load('images/alien_nd.bmp')
		if self.stats.level==3:
			self.image=pygame.image.load('images/alien_rd.bmp')
		if self.stats.level==4:
			self.image=pygame.image.load('images/alien_fourth.bmp')
		if self.stats.level>4:
			self.image=pygame.image.load('images/alien_fifth.bmp')

