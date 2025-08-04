import pygame
import json
class GameStats():
	def __init__(self,ai_game):
		self.setts=ai_game.setts
		self.high_score=self._read_record()
		self.reset_stats()
		self.game_active=False
	def reset_stats(self):
		self.level=1
		self.ships_left=self.setts.ship_limit
		self.setts.initialize_dynamic_settings()
		self.score=0
	def _read_record(self):
		f=open(self.setts.record_filename)
		rec=json.load(f)
		f.close()
		return rec