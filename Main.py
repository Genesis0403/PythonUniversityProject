import pygame as pg
import sys
from view.Window import Window
from entities.Entity import Entity

"""
	The game loop. Just testing.
"""

window = Window()
clock = pg.time.Clock()
pg.key.set_repeat(10,10)
size = [50,50]
speed = 3
entity = Entity(size)

while 1:
	clock.tick(60)
	window.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if pg.key.get_pressed()[pg.K_UP]:
			entity.move(0, -speed)
		if pg.key.get_pressed()[pg.K_DOWN]:
			entity.move(0, speed)
		if pg.key.get_pressed()[pg.K_RIGHT]:
			entity.move(speed, 0)
		if pg.key.get_pressed()[pg.K_LEFT]:
			entity.move(-speed, 0)
		entity.rotate()
		window.flip(entity)
		pg.display.update()

	
