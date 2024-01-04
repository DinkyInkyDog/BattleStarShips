
#I don't need this now But I might later.
#player_board = {"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "b": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "d": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "e": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "f": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "g": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "h": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "i": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

#don't get rid of that. I really need those letters.
letters = "abcdefghi"

#there will be two boards. One for the player and one for the enemy that print seperate and hold their own info
class Board:
    #this will be the player's board view
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    row_a = "| A  .    .    .    .    .    .    .    .    .     .    |"
    row_b = "| B  .    .    .    .    .    .    .    .    .     .    |"
    row_c = "| C  .    .    .    .    .    .    .    .    .     .    |"
    row_d = "| D  .    .    .    .    .    .    .    .    .     .    |"
    row_e = "| E  .    .    .    .    .    .    .    .    .     .    |"
    row_f = "| F  .    .    .    .    .    .    .    .    .     .    |"
    row_g = "| G  .    .    .    .    .    .    .    .    .     .    |"
    row_h = "| H  .    .    .    .    .    .    .    .    .     .    |"
    row_i = "| I  .    .    .    .    .    .    .    .    .     .    |"
    bottom = "_________________________________________________________"
    user_rows = [row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i]
    #I need a seperate board for each of the different versions that will happen.
    #so this next one will be the enemy board view
    e_top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    e_row_a = "| A  .    .    .    .    .    .    .    .    .     .    |"
    e_row_b = "| B  .    .    .    .    .    .    .    .    .     .    |"
    e_row_c = "| C  .    .    .    .    .    .    .    .    .     .    |"
    e_row_d = "| D  .    .    .    .    .    .    .    .    .     .    |"
    e_row_e = "| E  .    .    .    .    .    .    .    .    .     .    |"
    e_row_f = "| F  .    .    .    .    .    .    .    .    .     .    |"
    e_row_g = "| G  .    .    .    .    .    .    .    .    .     .    |"
    e_row_h = "| H  .    .    .    .    .    .    .    .    .     .    |"
    e_row_i = "| I  .    .    .    .    .    .    .    .    .     .    |"
    e_bottom = "_________________________________________________________"
    columndict = {1:5, 2:10, 3:15, 4:20, 5:25, 6:30, 7:35, 8:40, 9:45, 10:51}
    def __init__(self, enemy = False):
        self.fleet = {}
        self.enemy = enemy
        
    def mark_board(self, ship, list=letters):
        if ship.verticle == True:
            self.fleet[ship.name] = [ship.location.items()]
            #I need to figure out how to get that key out of the dictionary!!!
            index = 0
            row_letter = ""
            for letter in letters:
                if letter[index] in ship.location.keys():
                    row_letter = letter[index]
                    break
                else:
                    index += 1
            index = 0
            for r in self.user_rows:
                if row_letter.upper() in self.user_rows[index]:
                    #from here I need to know what numbers are needed to be marked so I can get the corisponding index for it.
                else:
                    index += 1
        else:
            rows = len(ship.location.keys())
            
                
        if self.enemy == False:
            ship.location

    def display(self):
        if self.enemy == False:
            print(self.top)
            print(self.row_a)
            print(self.row_b)
            print(self.row_c)
            print(self.row_d)
            print(self.row_e)
            print(self.row_f)
            print(self.row_g)
            print(self.row_h)
            print(self.row_i)
            print(self.bottom)
        if self.enemy == True:
            print(self.e_top)
            print(self.e_row_a)
            print(self.e_row_b)
            print(self.e_row_c)
            print(self.e_row_d)
            print(self.e_row_e)
            print(self.e_row_f)
            print(self.e_row_g)
            print(self.e_row_h)
            print(self.e_row_i)
            print(self.e_bottom)
       
       
player = Board()
enemy = Board(enemy=True)

def find_index(letter, list=letters):
    index = list.index(letter)
    return index

class Ship:
    verticle = True
    location = {}
    def __init__(self, size, rank = "(A)", status=True):
        self.size = size
        #The initialized ship is friendly by default, so when making the enemy ships change to false.
        self.friendly = status
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank
    def flip(self):
        if self.verticle == True:
            self.verticle = False
        else:
            self.verticle = True

    def assign_ship(self, letter, number, list=letters):
        if self.verticle == True:
            add = 0
            for mark in range(0, self.size):
                if letter not in self.location:
                    self.location[letter] = [number]
                    add += 1
                    continue
                self.location[letter].append(number + add)
                add += 1
        else:
            index = find_index(letter)
            for mark in range(0, self.size):
                self.location[letters[index]] = number
                index += 1

#player.display()
#enemy.display()

testship_1 = Ship(3)
#testship_1.flip()

testship_1.assign_ship("a", 4)
print(testship_1.location)
print(testship_1.name)

player.mark_board(testship_1)