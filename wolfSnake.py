import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#CC00CC'
COLOR_TAIL = '#CC00CC'



class WolfSnake(Snake):
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

        #print(self.coords[0] ,self.dx,self.dy, self.field.width,self.field.height)
        mis=list(self.field.mice.keys())
        x=self.coords[0][0]
        y=self.coords[0][1]
        mx=1000
        my=1000
        for (tx,ty) in mis:
            if abs(x-tx)+abs(y-ty)<abs(x-mx)+abs(y-my):
                mx=tx
                my=ty
        #print(mx,my)
        if self.coords[0][0] < mx:
            if self.dx!=1:
                if random.randint(0,10) < 5:
                    if random.randint(0,1) == 1:
                        self.turn_left()
                    else:
                        self.turn_right()
            

        elif self.coords[0][0] > mx:
            if self.dx!=-1:
                if random.randint(0,10) < 5:
                    if random.randint(0,1) == 1:
                        self.turn_left()
                    else:
                        self.turn_right()
        else:
            if self.coords[0][1] < my:
                if self.dy!=1:
                    if random.randint(0,10) < 5:
                        if random.randint(0,1) == 1:
                            self.turn_left()
                        else:
                            self.turn_right()
            elif self.coords[0][1] > my:
                if self.dy!=-1:
                    if random.randint(0,10) < 5:
                        if random.randint(0,1) == 1:
                            self.turn_left()
                        else:
                            self.turn_right()
        
