import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion():
	def __init__(self):
		pygame.init()
		self.setts=Settings()
		self.screen=pygame.display.set_mode(
			(0,0),pygame.FULLSCREEN)
		self.setts.screen_width=self.screen.get_rect().width
		self.setts.screen_height=self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.ship=Ship(self)
		self.bull=pygame.sprite.Group()
	def run_game(self):
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
	def _check_events(self):
		"""Managing user mouse and keyboard"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)
	def _check_keydown_events(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_r=True
		if event.key==pygame.K_LEFT:
			self.ship.moving_l=True
		if event.key==pygame.K_q:
			sys.exit()
		if event.key==pygame.K_SPACE:
			self._fire_bullet()
	def _check_keyup_events(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_r=False
		if event.key==pygame.K_LEFT:
			self.ship.moving_l=False
	def _fire_bullet(self):
		"""Creating new bullet and including it into bullets' group"""
		if len(self.bull)<self.setts.bullets_allowed:
			new_bullet=Bullet(self)
			self.bull.add(new_bullet)
	def _update_bullets(self):
		self.bull.update()
		for b in self.bull.copy():
			if b.rect.bottom <=0:
				self.bull.remove(b)
		#print(len(self.bull)) -debug
	def _update_screen(self):	
		self.screen.fill(self.setts.bg_color)
		self.ship.blitme()
		for b in self.bull.sprites():
			b.draw_bullet()
		pygame.display.flip()
if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()
