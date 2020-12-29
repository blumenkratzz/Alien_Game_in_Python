import pygame.font
class Scoreboard():
	def __init__(self,ai_game):
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.setts=ai_game.setts
		self.stats=ai_game.stats
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		self.prep_score()
	def prep_score(self):
		score_str=str(self.stats.score)
		self.score_image=self.font.render(score_str,True,
			self.text_color,self.setts.bg_color)
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=self.screen_rect.top+20
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)