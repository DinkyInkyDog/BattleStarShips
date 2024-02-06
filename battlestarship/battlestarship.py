
#This is the one I shall continue to work on.

#don't get rid of that.\/ I really need those letters.
letters = "abcdefghij"

class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10   |"""

    bottom = "_________________________________________________________"

    def __init__(self):
        self.fleet = []
        self.miss = []
        
    def display(self, enemy_board=False, letter=letters):
        enemy = enemy_board
        row_headers = ["| A", "| B", "| C", "| D", "| E", "| F", "| G", "| H", "| I", "| J"]
        if enemy == False:
            print(self.top)
            index = 0
            count = 1
            for header in row_headers:
                row = header
                for column in range(0, 10):
                    ship_located_here = False
                    for ships in self.fleet:
                        if [letter[index], count] in ships.location:
                            row += "  o  "
                            ship_located_here = True
                            break
                        if [letter[index], count] in ships.hit:
                            row += "  X  "
                            ship_located_here = True
                            break
                    if ship_located_here == False:
                        row += "  .  "
                    count += 1
                index += 1
                count = 1
                row += "  |"
                print(row)   
            print(self.bottom)
        else:
            print(self.top)
            index = 0
            count = 1
            for header in row_headers:
                row = header
                for column in range(0, 10):
                    something_found = False
                    for ships in self.fleet:
                        if [letter[index], count] in ships.hit:
                            row += "  X  "
                            something_found = True
                            break
                        if [letter[index], count] in self.miss:
                            row += '  *  '
                            something_found = True
                            break
                    if something_found == False:
                        row += "  .  "
                    count += 1
                index += 1
                count = 1
                row += "  |"
                print(row)
            print(self.bottom)


    def attack(self, r, c, board_being_attacked, letters=letters):
        target_hit = False
        for ship in board_being_attacked.fleet:
            if [r, c] in ship.location:
                target_hit = True
                ship.location.remove([r, c])
                ship.hit.append([r, c])
                print("You Hit!!")
                break
        if target_hit == False:
            self.miss.append([r, c])
            print("You missed...")
            
            
run_game = True
player = Board()
enemy = Board()


class Ship:
    
    alive = True
    def __init__(self, size, rank = "(A)"):
        self.location = []
        self.hit = []
        self.size = size
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank

    def assign_ship(self, letter, number, board, verticle = True, up = False, left = False, list=letters):
        board.fleet.append(self)
        self.verticle = verticle
        starting_letter_index = letters.index(letter)
        if self.verticle == True and up == False:
            if self.size + number > 10 or self.size + starting_letter_index > 9:
                print("------------------Failed to asign----------------------")
                print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index += 1
        if self.verticle == True and up == True:
            if self.size - number <= 0 or self.size - starting_letter_index < 0:
                print("------------------Failed to asign----------------------")
                print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index -= 1

        if self.verticle == False:
            if left == True:
                if number - self.size <= 0:
                    print("------------------Failed to asign----------------------")
                    print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                    return False
                else:
                    num = number
                    for location in range(0, self.size):
                        self.location.append([letter, num])
                        num -= 1
            else:
                if number + self.size > 10:
                    print("------------------Failed to asign----------------------")
                    print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                    return False
                else:
                    num = number
                    for location in range(0, self.size):
                        self.location.append([letter, num])
                        num += 1
        


    def __repr__(self):
        stats = """Ship Name: {name}
         Ship Location: {location} """.format(name=self.name, location=self.location)

        return stats


ship_1 = Ship(4, "(A)")
ship_1.assign_ship("b", 6, player, False, False, True)
print(player.fleet)

enemy.attack('b', 4, player)


 