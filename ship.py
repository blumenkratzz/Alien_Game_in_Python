import pygame
class Ship():
	def __init__(self,ai_game):
		self.screen=ai_game.screen
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
		if self.moving_r==True:
			self.x+=1
		if self.moving_l==True:
			self.x-=1
		self.rect.x=self.x