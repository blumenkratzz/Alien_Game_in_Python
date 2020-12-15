import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
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
		self.aliens=pygame.sprite.Group()
		self._create_fleet()
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
		"""Update position and remove irrelevant bullets"""
		self.bull.update()
		for b in self.bull.copy():
			if b.rect.bottom <=0:
				self.bull.remove(b)
		#print(len(self.bull)) -debug
	def _create_fleet(self):
		new_alien=Alien(self)
		alien_width=new_alien.rect.width
		alien_height=new_alien.rect.height
		ship_height=self.ship.rect.height
		available_space_x=(self.setts.screen_width-
			(2*alien_width))
		available_space_y=(self.setts.screen_height-
			(3*alien_height)-ship_height)
		number_aliens_x=available_space_x//(2*alien_width)
		number_rows=available_space_y//(2*alien_height)
		for row in range(number_rows):
			for al in range(number_aliens_x):
				self._create_alian(al,row)
			
	def _create_alian(self,al_number,row_number):
		new_alien=Alien(self)
		alien_width=new_alien.rect.width
		new_alien.x=alien_width+alien_width*2*al_number
		new_alien.rect.x=new_alien.x
		new_alien.rect.y=(new_alien.rect.height+
			2*new_alien.rect.height)#*row_number)
		self.aliens.add(new_alien)
	def _update_screen(self):	
		self.screen.fill(self.setts.bg_color)
		self.ship.blitme()
		for b in self.bull.sprites():
			b.draw_bullet()
		self.aliens.draw(self.screen)
		pygame.display.flip()
if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()
