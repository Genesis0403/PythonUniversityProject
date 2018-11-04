import pygame as pg
import sys
from view.Window import Window
from entities.Entity import Entity
from entities.Bullet import Bullet


window = Window()
clock = pg.time.Clock()
pg.key.set_repeat(10, 10)
size = [100,100]
speed = 5
entity = Entity(size)
entities = pg.sprite.Group()
entities.add(entity)
bullets = pg.sprite.Group()
bullet_timer = 0

while 1:
	clock.tick(60)
	dt = clock.tick(60) / 1000
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if pg.key.get_pressed()[pg.K_w]:
			entity.move(0, -speed)
		if pg.key.get_pressed()[pg.K_s]:
			entity.move(0, speed)
		if pg.key.get_pressed()[pg.K_d]:
			entity.move(speed, 0)
		if pg.key.get_pressed()[pg.K_a]:
			entity.move(-speed, 0)
		if pg.mouse.get_pressed()[0]:
			if (bullet_timer - dt <= 0):
				bullet_timer = 0
				pos, angle = entity.position(), entity.angle
				bullets.add(Bullet(pos, angle, 20))
			bullet_time = 0.1

	window.update()
	entities.update()
	bullets.update()
	window.update_entities(entities)
	window.update_bullets(bullets)
	#allsprites.draw(window.screen)
	pg.display.update()

	
