import pygame

class Tetromino:
    def __init__(self, g):
        self.settings = g.settings
        self.grid = g.grid
        self.n = self.settings.n_of_col -1
        self.pos = []
        self.current_rot = 0

    def check_down(self):
        for i in self.pos:
            if i[0] == 21:
                return True 
            
    def check_touch(self):
        for i in self.pos:
            if self.grid[i[0]+1][i[1]] != 0 and [(i[0]+1),i[1]] not in self.pos:
                return True 
            
    def clear(self):
        for i in self.pos:
            self.grid[i[0]][i[1]] = 0

    def check_if_any_on_col0(self):
        for i in self.pos:
            if i[1] == 0:
                return True
            
    def check_if_any_on_last_col(self):
        for i in self.pos:
            if i[1] == self.n:
                return True
            
    def rotate_left(self):
        self.clear()
        if self.current_rot == 0 and self.main_pos[0] != self.settings.n_of_rows -1:
            self.pos3()
            self.current_rot = 3
        elif self.current_rot == 1 and self.main_pos[1] != 0:
            self.pos0()
            self.current_rot = 0
        elif self.current_rot == 2:
            self.pos1()
            self.current_rot = 1
        elif self.current_rot == 3 and self.main_pos[1] != self.n:
            self.pos2()
            self.current_rot = 2

    def rotate_right(self):
        self.clear()
        if self.current_rot == 0 and self.main_pos[0] != self.settings.n_of_rows -1:
            self.pos1()
            self.current_rot = 1
        elif self.current_rot == 1  and self.main_pos[1] != 0:
            self.pos2()
            self.current_rot = 2
        elif self.current_rot == 2:
            self.pos3()
            self.current_rot = 3
        elif self.current_rot == 3  and self.main_pos[1] != self.n:
            self.pos0()
            self.current_rot = 0

    def move_right(self):
        if self.check_if_any_on_last_col():
            return
        self.clear()
        for i in self.pos:
            i[1] += 1

    def move_left(self):
        if self.check_if_any_on_col0():
            return
        self.clear()
        for i in self.pos:
            i[1] -= 1
    
    def move_down(self):      
        self.clear()
        for i in self.pos:
            i[0] += 1

class Itetromino(Tetromino):
    def __init__(self,g):
        super().__init__(g)
        self.color = self.settings.I_color
        self.spawn()
        self.put_on_grid()

    def spawn(self):
        self.pos = [[1, self.n//2-1],[1, self.n//2],[1, self.n//2+1],[1, self.n//2+2]]

    def put_on_grid(self):
        for i in self.pos:
            self.grid[i[0]][i[1]] = "I"

    def rotate_right(self):
        self.clear()
        if self.current_rot == 0 and self.pos[0][0]<self.settings.n_of_rows-2:
            self.pos[0][0] -= 1
            self.pos[0][1] += 2
            self.pos[1][0] += 1
            self.pos[1][1] += 1
            self.pos[3][0] += 2
            self.pos[3][1] -= 1
            self.current_rot = 1
        elif self.current_rot == 1 and self.pos[0][1]<self.n and self.pos[0][1]>1:
            self.pos[0][0] += 2
            self.pos[0][1] -= 2
            self.pos[2][0] += 1
            self.pos[2][1] -= 1
            self.pos[3][0] -= 1
            self.pos[3][1] += 1
            self.current_rot = 2
        elif self.current_rot == 2 and self.pos[0][0]<self.settings.n_of_rows-1:
            self.pos[0][0] -= 2
            self.pos[0][1] += 1
            self.pos[1][0] -= 1
            self.pos[1][1] -= 1
            self.pos[3][0] += 1
            self.pos[3][1] -= 2
            self.current_rot = 3
        elif self.current_rot == 3  and self.pos[0][1]<self.n -1 and self.pos[0][1]>0:
            self.pos[0][0] += 1
            self.pos[0][1] -= 1
            self.pos[2][0] -= 1
            self.pos[2][1] += 1
            self.pos[3][0] -= 2
            self.pos[3][1] += 2
            self.current_rot = 0

    def rotate_left(self):
        self.clear()
        if self.current_rot == 0 and self.pos[0][0]<self.settings.n_of_rows-2:
            self.pos[0][0] -= 1
            self.pos[0][1] += 1
            self.pos[2][0] += 1
            self.pos[2][1] -= 1
            self.pos[3][0] += 2
            self.pos[3][1] -= 2
            self.current_rot = 3
        elif self.current_rot == 1  and self.pos[0][1]<self.n and self.pos[0][1]>1:
            self.pos[0][0] += 1
            self.pos[0][1] -= 2
            self.pos[1][0] -= 1
            self.pos[1][1] -= 1
            self.pos[3][0] -= 2
            self.pos[3][1] += 1
            self.current_rot = 0
        elif self.current_rot == 2 and self.pos[0][0]<self.settings.n_of_rows-1:
            self.pos[0][0] -= 2
            self.pos[0][1] += 2
            self.pos[2][0] -= 1
            self.pos[2][1] += 1
            self.pos[3][0] += 1
            self.pos[3][1] -= 1
            self.current_rot = 1
        elif self.current_rot == 3 and self.pos[0][1]<self.n -1 and self.pos[0][1]>0:
            self.pos[0][0] += 2
            self.pos[0][1] -= 1
            self.pos[1][0] += 1
            self.pos[1][1] += 1
            self.pos[3][0] -= 1
            self.pos[3][1] += 2
            self.current_rot = 2

class Otetromino(Tetromino):
    def __init__(self,g):
        super().__init__(g)
        self.color = self.settings.O_color
        self.spawn()
        self.put_on_grid()

    def spawn(self):
        self.pos = [[1, self.n//2-1],[1, self.n//2],[1, self.n//2+1],[1, self.n//2+2]]

    def put_on_grid(self):
        for i in self.pos:
            self.grid[i[0]][i[1]] = "I"

    def pos0(self, dir):
        if dir == "left":
            pass
        elif dir == "right":
            pass

    def pos0(self, dir):
        if dir == "left":
            pass
        elif dir == "right":
            pass

    def pos0(self, dir):
        if dir == "left":
            pass
        elif dir == "right":
            pass

    def pos0(self, dir):
        if dir == "left":
            pass
        elif dir == "right":
            pass

class Ttetromino(Tetromino):
    def __init__(self,g):
        super().__init__(g)
        self.color = self.settings.T_color
        self.spawn()
        self.put_on_grid()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [[1, self.n//2-2],[1, self.n//2-1],[1, self.n//2],[0, self.n//2-1]]

    def put_on_grid(self):
        self.main_pos = self.pos[1]
        for i in self.pos:
            self.grid[i[0]][i[1]] = "T"

    def pos0(self):
        self.pos[0][0] = self.main_pos[0]-1
        self.pos[0][1] = self.main_pos[1]
        self.pos[2][0] = self.main_pos[0]
        self.pos[2][1] = self.main_pos[1]+1
        self.pos[3][0] = self.main_pos[0]
        self.pos[3][1] = self.main_pos[1]-1

    def pos1(self):
        self.pos[0][0] = self.main_pos[0]-1
        self.pos[0][1] = self.main_pos[1]
        self.pos[2][0] = self.main_pos[0]+1
        self.pos[2][1] = self.main_pos[1]
        self.pos[3][0] = self.main_pos[0]
        self.pos[3][1] = self.main_pos[1]+1

    def pos2(self):
        self.pos[0][0] = self.main_pos[0]
        self.pos[0][1] = self.main_pos[1]-1
        self.pos[2][0] = self.main_pos[0]+1
        self.pos[2][1] = self.main_pos[1]
        self.pos[3][0] = self.main_pos[0]
        self.pos[3][1] = self.main_pos[1]+1

    def pos3(self):
        self.pos[0][0] = self.main_pos[0]-1
        self.pos[0][1] = self.main_pos[1]
        self.pos[2][0] = self.main_pos[0]+1
        self.pos[2][1] = self.main_pos[1]
        self.pos[3][0] = self.main_pos[0]
        self.pos[3][1] = self.main_pos[1]-1