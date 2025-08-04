import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.setts=ai_game.setts
		self.screen_rect=ai_game.screen.get_rect()
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.rect.midbottom=self.screen_rect.midbottom
		self.moving_r=False
		self.moving_l=False
		self.x=float(self.rect.x)
	def blitme(self):
		"""Drawing the ship in the current position"""
		self.screen.blit(self.image,self.rect)
	def update(self):
		"""Update position of the ship according to the flag"""
		if self.moving_r==True and self.rect.right<self.screen_rect.right:
			self.x+=self.setts.ship_speed
		if self.moving_l==True and self.rect.left>self.screen_rect.left:
			self.x-=self.setts.ship_speed
		self.rect.x=self.x
	def center_ship(self):
		self.rect.midbottom=self.screen_rect.midbottom
		self.x=float(self.rect.x)