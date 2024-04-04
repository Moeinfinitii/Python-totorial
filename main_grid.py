import random
class Grid:
    def __init__(self):
        self.board_s = 10
        self.mine_nums = 10
        self.cell_mines = []
        

    def setup(self):
        self.board_size()
        # self.number_of_mine()
        self.game_difficulty()
        self.cell_list()
        self.get_numbers()
        self.print_test()
    
    def board_size(self):
        print('Please enter size of the game (between 3 and 10):')
        while True:
            size = input ('')
            try:
                self.board_s = int(size)
                if self.board_s > 10 or self.board_s < 3:
                    print("Your number isn't between 3 and 10:")
                else:
                    break
            except:
                print('Enter a number:')

    def game_difficulty(self):
        print('Select difficulty: 1.Easy 2.Medium 3.Hard')
        while True:
            level_input = input('')   
            try:
                level_input = int(level_input)

                if level_input == 1:
                    self.mine_nums = self.board_s
                    break
                if level_input == 2:
                    self.mine_nums = round(self.board_s * 1.5)
                    break
                if level_input == 3:
                    self.mine_nums = self.board_s * 2
                    break
                else:
                    print('Please select 1,2 or 3:')
            except:
                print('Please enter a number')
        # print(self.mine_nums)
                




    def number_of_mine(self):
        print(f'Please enter number of mines (between 0 and {self.board_s ** 2}):')
        while True:
            size = input ('')
            try:
                self.mine_nums = int(size)
                if  self.mine_nums <= 0 or  self.mine_nums > self.board_s ** 2:
                    print(f"Your number isn't between 0 and {self.board_s ** 2}:")
                else:
                    break
            except:
                print('Enter a number:')
        return self.board_s   
    

    def cell_list(self):
        self.cell = [[' '] * self.board_s for i in range(self.board_s)]
        for k in range(self.mine_nums):
            i = random.randint(0,self.board_s-1)
            j = random.randint(0,self.board_s-1)

            if [i,j] not in self.cell_mines:
                self.cell[i][j] = 'm'
            self.cell_mines.append([i,j])
        # print(self.cell)

        # k = 0 
        # self.board_size()
        # print(self.cell)
        # for i in range(self.board_s):
        #     for j in range(self.board_s):
        #         if k<= self.mine_nums:
        #             self.cell[i][j] = 'm'
        #             k += 1
        # random.shuffle(self.cell)
        # print(self.cell)

    
    def get_numbers(self):
        for i in range(self.board_s):
            for j in range(self.board_s):
                k = 0

                # Top - Left
                try:
                    if [i-1,j-1] in self.cell_mines:
                        k+=1
                except:
                    pass

                # Top - Middle
                try:
                    if [i-1,j] in self.cell_mines:
                        k+=1
                except:
                    pass

                # Top - Right
                try:
                    if [i-1,j+1] in self.cell_mines:
                        k+=1
                except:
                    pass
                
                # Middle - Left
                try:
                    if [i,j-1] in self.cell_mines:
                        k+=1
                except:
                    pass
                
                # Middle - Right 
                try:
                    if [i,j+1] in self.cell_mines:
                        k+=1
                except:
                    pass

                # Bottom - Left
                try:
                    if [i+1,j-1] in self.cell_mines:
                        k+=1
                except:
                    pass
                
                #Bottom - Middle
                try:
                    if [i+1,j] in self.cell_mines:
                        k+=1
                except:
                    pass
                
                # Bottom - Right
                try:
                    if [i+1,j+1] in self.cell_mines:
                        k+=1
                except:
                    pass

                # Self cell check
                try:
                    if [i,j] in self.cell_mines:
                        k = 10
                except:
                    pass
                
                
                if k != 10:
                    self.cell[i][j] = k
        
    def print_test(self):
        for i in range(self.board_s):
            print(self.cell[i])

        

my_obj = Grid()
my_obj.setup()
