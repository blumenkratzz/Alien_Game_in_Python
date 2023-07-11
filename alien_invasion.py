import sys
import json
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion():
	def __init__(self):
		pygame.init()
		self.setts=Settings()
		self.screen=pygame.display.set_mode(
			(0,0))#,pygame.FULLSCREEN)
		self.setts.screen_width=self.screen.get_rect().width
		self.setts.screen_height=self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.play_button=Button(self,"Play")
		pygame.mixer.music.load('music/background_XX_intro.mp3')
		pygame.mixer.music.play(-1)
		self.sound_ship_attack=pygame.mixer.Sound('music/ship_attack.mp3')
		self.sound_ship_attack.set_volume(0.2)
		self.sound_level_success=pygame.mixer.Sound('music/new_level.mp3')
		self.sound_level_failure=pygame.mixer.Sound('music/failure_level.mp3')
		self.sound_level_failure.set_volume(0.6)
		self.sound_alien_ship=pygame.mixer.Sound('music/alien_ship_collision.mp3')
		self.sound_alien_ship.set_volume(0.3)
		self.stats=GameStats(self)
		self.sb=Scoreboard(self)
		self.ship=Ship(self)
		self.bull=pygame.sprite.Group()
		self.aliens=pygame.sprite.Group()
		self._create_fleet()
	def run_game(self):
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
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
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
	def _check_play_button(self,mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
			self.stats.reset_stats()
			self.stats.game_active=True
			self.aliens.empty()
			self.bull.empty()
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)
			self.sb.prep_level()
			self.sb.prep_ships()

	def _check_keydown_events(self,event):
		if event.key==pygame.K_ESCAPE:
			if self.stats.game_active==False:
				self.stats.game_active=True
			else:
				self.stats.game_active=False
		if event.key==pygame.K_RIGHT:
			self.ship.moving_r=True
		if event.key==pygame.K_LEFT:
			self.ship.moving_l=True
		if event.key==pygame.K_q:
			self._write_record(self.stats.high_score)
			sys.exit()
		if event.key==pygame.K_SPACE and self.stats.game_active:
			self.sound_ship_attack.play()
			self._fire_bullet()
		if event.key==pygame.K_1:
			pygame.mixer.music.pause()
		if event.key==pygame.K_2:
			pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()*0.5)
		if event.key==pygame.K_3:
			pygame.mixer.music.unpause()
			pygame.mixer.music.set_volume(1)
		if event.key==pygame.K_s:
			if self.stats.game_active:
				if self.stats.ships_left>0:
					self.stats.ships_left-=1
					self.sb.prep_ships()
			if self.stats.ships_left==0:
				self.stats.game_active=False
				self.sound_level_failure.play()
				self.stats.reset_stats()
				self.sb.prep_score()
				pygame.mouse.set_visible(True)
	def _check_keyup_events(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_r=False
		if event.key==pygame.K_LEFT:
			self.ship.moving_l=False
	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
	def _check_aliens_bottom(self):
		screen_rect=self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom>=screen_rect.bottom:
				self._ship_hit()
				break
	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y+=self.setts.fleet_drop_speed
		self.setts.fleet_direction*=-1
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
		self._check_bullet_alien_collisions()
		#print(len(self.bull)) -debug
	def _check_bullet_alien_collisions(self):
		collisions=pygame.sprite.groupcollide(
			self.bull,self.aliens,True,True)
		if collisions:
			for al in collisions.values():
				self.stats.score+=self.setts.alien_points*len(al)
			self.sb.prep_score()
			self.sb.check_high_score()
		if not self.aliens:
			self.bull.empty()
			self.setts.increase_speed()
			self.sound_level_success.play()
			self.stats.level+=1
			self.sb.prep_level()
			self._create_fleet()
	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()
		"""check alien-ship collision"""
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()
	def _ship_hit(self):
		if self.stats.ships_left > 0:
			self.stats.ships_left-=1
			self.sound_alien_ship.play()
			self.sb.prep_ships()
			self.aliens.empty()
			self.bull.empty()
			self._create_fleet()
			self.ship.center_ship()
			sleep(1)
		if self.stats.ships_left==0:
			self.stats.game_active=False
			self.sound_level_failure.play()
			self.stats.reset_stats()
			self.sb.prep_score()
			pygame.mouse.set_visible(True)
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
			2*new_alien.rect.height*row_number)
		self.aliens.add(new_alien)
	def _write_record(self,record):
		filename=self.setts.record_filename
		f=open(filename,'w')
		json.dump(record,f)
		f.close()
	def _update_screen(self):	
		self.screen.fill(self.setts.bg_color)
		self.ship.blitme()
		for b in self.bull.sprites():
			b.draw_bullet()
		self.aliens.draw(self.screen)
		self.sb.show_score()
		if not self.stats.game_active:
			self.play_button.draw_button()
		pygame.display.flip()
if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()
