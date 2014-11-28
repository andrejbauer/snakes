# -*- encoding: utf-8 -*-

import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#009900'
COLOR_TAIL = '#007A29'

class SeaSnake(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute

    def turn(self):
        """Igrica poklice metodo turn vsakic, preden premakne kaco. Kaca naj se tu odloci, ali se
           bo obrnila v levo, v desno, ali pa bo nadaljevala pot v isti smeri.

           * v levo se obrne s self.turn_left()
           * v desno se obrne s self.turn_right()
           * koordinate glave so self.coords[0]
           * smer, v katero potuje je (self.dx, self.dy)
           * spisek koordinat vseh misk je self.field.mice.keys()
           * spisek vseh kac je self.field.snakes
        """
        # koordinate glave kače
        [gx, gy] = self.coords[0]

        if self.field.is_mouse(gx + self.dx, gy + self.dy):
            pass
        elif self.field.is_mouse(gx - self.dy, gy + self.dx):
            self.turn_left()
        elif self.field.is_mouse(gx + self.dy, gy - self.dx):
            self.turn_right()
        elif not self.field.is_empty(gx + self.dx, gy + self.dy):
            if not self.field.is_empty(gx - self.dy, gy + self.dx):
                self.turn_right()
            else:
                self.turn_left()
