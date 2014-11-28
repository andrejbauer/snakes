import random
from snake import *

# Barva glave in repa
COLOR_HEAD = 'green'
COLOR_TAIL = 'brown'

class Viper(Snake):
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
            
           
        if random.randint(0,5) < 5:
            if (self.dx, self.dy) == self.field.mice.keys() or (self.dx, self.dy)==self.field.snakes:
                    self.turn_left()
            else:
                if random.randint(0,1) == 1:
                    self.turn_left()
                else:
                    self.turn_right()
