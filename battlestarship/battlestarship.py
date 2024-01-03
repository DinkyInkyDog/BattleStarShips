
#I don't need this now But I might later.
#player_board = {"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "b": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "d": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "e": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "f": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "g": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "h": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "i": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}


letters = "abcdefghi"

#there will be two boards. One for the player and one for the enemy that print seperate and hold their own info
class Board:
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
    def __init__(self, enemy = False):
        self.fleet = []
        self.enemy = enemy
    def generate_board(self):
        row_a = "| A"
        #I need to have i go through the fleet's locations and know if any of them are in the spaces
        for ship in fleet:
            pass
       
       


def find_index(letter, list=letters):
    index = list.index(letter)
    return index

class Ship:
    verticle = True
    location = {}
    def __init__(self, size, status=True):
        self.size = size
        #The initialized ship is friendly by default, so when making the enemy ships change to false.
        self.friendly = status

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

testship_1 = Ship(3)
#testship_1.flip()

testship_1.assign_ship("a", 4)
print(testship_1.location)

