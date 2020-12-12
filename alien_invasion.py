import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion():
	def __init__(self):
		pygame.init()
		self.setts=Settings()
		self.screen=pygame.display.set_mode(
			(self.setts.screen_width,self.setts.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship=Ship(self)
	def run_game(self):
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()
	def _check_events(self):
		"""Managing user mouse and keyboard"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					self.ship.moving_r=True
				if event.key==pygame.K_LEFT:
					self.ship.moving_l=True
			elif event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT:
					self.ship.moving_r=False
				if event.key==pygame.K_LEFT:
					self.ship.moving_l=False
	def _update_screen(self):	
		self.screen.fill(self.setts.bg_color)
		self.ship.blitme()
		pygame.display.flip()
if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()
