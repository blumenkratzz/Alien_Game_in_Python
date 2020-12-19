import pygame
class GameStats():
	def __init__(self,ai_game):
		self.setts=ai_game.setts
		self.reset_stats()
		self.game_active=False
	def reset_stats(self):
		self.ships_left=self.setts.ship_limit