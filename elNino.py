import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#009933'
COLOR_TAIL = '#FF00FF'

class ElNino(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute

    def d(self, u, v):
        return abs(u[0] - v[0]) + abs(u[1] - v[1])

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

        # Choose closest item
        dist = float('inf')
        goal = None

        if len(self.field.mice) == 0: return
        
        for food in self.field.mice.keys():
            if self.d(food, self.coords[0]) < dist:
                dist = self.d(food, self.coords[0])
                goal = food

        w, h = self.field.width, self.field.height
        grid = [[True for i in range(h)] for j in range(w)]
        for kaca in self.field.snakes:
            for u, v in kaca.coords:
                grid[u][v] = False
        for u, v in self.coords:
                grid[u][v] = False
        x, y = self.coords[0]
        grid[x][y] = True
        # print(grid)
        graph = {(i, j):[] for i in range(1, w) for j in range(1, h)
                 if grid[i][j] == True}

        for g in graph:
            for (du, dv) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                sos = (g[0] + du, g[1] + dv)
                if sos in graph:
                    graph[g].append(sos)

        # print(graph)

        def vec_plus(a, b):
            return (a[0] + b[0], a[1] + b[1])

        ne = self.shortest_path(graph, self.coords[0], goal)
        if ne == 'Screwed':
            if len(self.coords) > 1:
                del self.coords[-1]
            return
        lx, ly = -self.dy, self.dx

        if random.randint(1, 2) == 1:
            
            if ne == vec_plus(self.coords[0], (self.dx, self.dy)):
                pass # do nothing
            elif ne == vec_plus(self.coords[0], (lx, ly)):
                self.turn_left()
            else:
                self.turn_right()
        else:
            if ne == vec_plus(self.coords[0], (self.dx, self.dy)):
                pass # do nothing
            elif ne != vec_plus(self.coords[0], (lx, ly)):
                self.turn_right()
            else:
                self.turn_left()
    
    def shortest_path(self, gr, beg, end):
        # print(gr)
        # raise KeyError
        seen = {beg}
        queue = [beg]
        parent = {beg: None}
        while queue:
            u = queue.pop(0)
            # print(gr[u])
            for v in gr[u]:
                if v in seen: continue
                parent[v] = u
                seen.add(v)
                queue.append(v)

        if end not in parent:
            return "Screwed"
        path = [end]
        while path[-1] != beg:
            path.append(parent[path[-1]])
        return list(reversed(path))[1]
