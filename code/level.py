import pygame
from setting import *
from tile import Tile
from player import Player
class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = pygame.sprite.Group()
		self.obstacles_sprites = pygame.sprite.Group()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x=row_index * TILESIZE
				y=col_index * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visible_sprites])
				if col == 'p':
					Player((x,y),self.visible_sprites)
	def run(self):
		self.visible_sprites.draw(self.display_surface)