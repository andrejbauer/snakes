import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#00FFF2'
COLOR_TAIL = '#99FF00'

class BlueKrait(Snake):
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

        # Koordinate glave
        (x,y) = self.coords[0]
        # Smer gibanja
        (sx,sy)=(self.dx, self.dy)

        self.grow = 1

        if not self.field.is_empty(x+sx,y+sy):
            if random.randint(0,1)>0:
                self.turn_right()
            else:
                self.turn_left()
        
