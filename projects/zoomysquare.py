import pygame as pg

class GameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pg.init()
        pg.display.set_caption(title)
        screen = pg.display.set_mode(resolution, pg.SCALED | pg.RESIZABLE)
        clock = pg.time.Clock()
        frame = 0
        self.running = True
        while self.running:
            clock.tick(fps)
            self.keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                    self.running = False
                if event.type == pg.VIDEORESIZE:
                    pg.display._resize_event(event)
                if (self.keys[pg.K_RALT] or self.keys[pg.K_LALT]) and self.keys[pg.K_RETURN]:
                    pg.display.toggle_fullscreen()
            screen.fill(color_background)
            self.loop(screen, frame)
            pg.display.flip()
            frame += 1
        self.quit()
        pg.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown


class Game(GameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.xmove = 1
        self.ymove = 1
        self.image = pg.image.load('zoomysquare.bmp')
        super().__init__()
    def loop(self, screen, frame):
        screen.blit(self.image, (self.x, self.y))

# class Game(GameBase):
#     def __init__(self):
#         self.x = 100
#         self.y = 100
#         self.xmove = 1
#         self.ymove = 1
#         super().__init__()

    def loop(self, screen, frame):
        if self.x >= screen.get_width() - 50 or self.x <= 0:
            self.xmove = -self.xmove
        if self.xmove == 1:
            self.x += 1
        if self.xmove == -1:
            self.x += -1
        if self.y >= screen.get_height() - 50 or self.y <= 0:
            self.ymove = -self.ymove
        if self.ymove == 1:
            self.y += 1
        if self.ymove == -1:
            self.y += -1
#        image = pg.image.load('zoomysquare.bmp').convert()
        screen.blit(self.image, (self.x, self.y))
#        pg.draw.rect(screen, 'red', (self.x, self.y, 50, 50), 2, border_radius=0)

# 1.) Square edged red rectangle - 50 50
# 2.) it moves automatically
# 3.) DVD screensaver - bounces off top bottom left right

if __name__ == '__main__':
    Game()