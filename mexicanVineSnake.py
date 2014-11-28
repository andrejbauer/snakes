import random
from snake import *

# Barva glave in repa
COLOR_HEAD = 'pink'
COLOR_TAIL = 'red'

class MexicanVineSnake(Snake):
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
        koord=self.coords[0]
        smer=(self.dx, self.dy)
        polje=self.field
        if smer==(0,-1):
            if polje.is_empty( koord[0]+1, koord[1]):
                self.turn_right()
            elif polje.is_empty( koord[0]-1, koord[1]):
                self.turn_left()
            else:
                pass
        if smer==(0,1):
            if polje.is_empty(koord[0]+1, koord[1]):
                self.turn_left()
            elif polje.is_empty( koord[0]-1, koord[1]):
                self.turn_right()
            else:
                pass
        if smer==(-1,0):
            if polje.is_empty( koord[0], koord[1]+1):
                self.turn_right()
            elif polje.is_empty( koord[0], koord[1]-1):
                self.turn_left()
            else:
                pass
        if smer==(1,0):
            if polje.is_empty(koord[0], koord[1]+1):
                self.turn_left()
            elif polje.is_empty( koord[0], koord[1]-1):
                self.turn_right()
            else:
                pass
##        if random.randint(0,10) < 5:
##            if random.randint(0,1) == 1:
##                self.turn_left()
##            else:
##                self.turn_right()
