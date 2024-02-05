
#This is the one I shall continue to work on.
#don't get rid of that.\/ I really need those letters.
letters = "abcdefghij"
#there will be two boards. One for the player and one for the enemy that print seperate and hold their own info
class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10   |"""
    row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    bottom = "_________________________________________________________"
    user_rows = [row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i]
    #I need a seperate board for each of the different versions that will happen.
    #so this next one will be the enemy board view
    e_top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10   |"""
    e_row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  |"]
    e_bottom = "_________________________________________________________"
    enemy_rows = [e_row_a, e_row_b, e_row_c, e_row_d, e_row_e, e_row_f, e_row_g, e_row_h, e_row_i]
    def __init__(self, enemy = False):
        self.fleet = {}
        self.enemy = enemy
        self.ships = []


    def display(self):
        if self.enemy == False:
            print(self.top)
            for row in self.user_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.bottom)
        
        if self.enemy == True:
            print(self.e_top)
            for row in self.enemy_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.e_bottom) 

                
        else:
            self.ships.append(ship)
            self.fleet[ship] = [item for sublist in ship.location.items() for item in sublist]
            index = 0
            row_letters = []
            for letter in letters:
                if letters[index] in ship.location.keys():
                    row_letters.append(letters[index])
                    index += 1
                else:
                    index += 1
            column_number = 0
            for num in ship.location.values():
                    column_number = num
           
            if self.enemy == False:
                index_2 = 0
                for row in range(0, len(row_letters)):
                    i = letters.find(row_letters[index_2])
                    row = self.user_rows[i]
                    row.pop(column_number)
                    row.insert(column_number, "  o  ")
                    index_2 += 1
            #self.display()

    def attack(self, r, c, board_being_attacked, letters=letters):
        values = [value for sublist in board_being_attacked.fleet.values() for value in sublist]
        
        list_values = []
        for item in values:
            if isinstance(item, list):
                for n in item:
                    list_values.append(n)
            else:
                list_values.append(item)

        hit = False
        if r in list_values and c in list_values:
            hit = True
            if self.enemy == False:
                i = letters.find(r)
                row= board_being_attacked.enemy_rows[i]
                row.pop(c)
                row.insert(c, "  X  ")
                board_being_attacked.display()
                print("you hit!")
            else:
                i = letters.find(r)
                row= board_being_attacked.user_rows[i]
                row.pop(c)
                row.insert(c, "  X  ")
                board_being_attacked.display()
                print("you've been hit!")
        else:
            if self.enemy == True:
                i = letters.find(r)
                row= board_being_attacked.user_rows[i]
                row.pop(c)
                row.insert(c, "  *  ")
                board_being_attacked.display()
                print("miss")
            else:
                i = letters.find(r)
                row= board_being_attacked.enemy_rows[i]
                row.pop(c)
                row.insert(c, "  o  ")
                board_being_attacked.display()
                print("miss") 
        #Okay so marking the board works. Just need to damage the ship.
        if hit == True:
            for ship in board_being_attacked.ships:
                #print(ship)
                #print(ship.health)
                if ship.location.get(r, False) != False:
                    n = ship.location[r]
                    if isinstance(n, list):
                        for number in n:
                            if number == c:
                                ship.take_damage()
                    else:
                        if n == c:
                            ship.take_damage()
                if ship.alive == False:
                    board_being_attacked.ships.remove(ship)
                    board_being_attacked.fleet.pop(ship)
                    
    def check_defeat(self):
        if len(self.ships) == 0:
            return True
        else:
            return False
            
run_game = True                    


       
       
player = Board()
enemy = Board(enemy=True)


class Ship:
    
    alive = True
    def __init__(self, size, rank = "(A)"):
        self.location = []
        self.hit = []
        self.size = size
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank

    def assign_ship(self, letter, number, verticle = True, up = False, left = False, list=letters):
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
        

#need to change this so that it'll show the locations and health of the ships. 
    def __repr__(self):
        stats = " "
        return stats


ship_1 = Ship(4, "(A)")
ship_1.assign_ship("b", 6, False, False, True)
print(ship_1.location)



    
#make a random generator so that the enemy ships are in a different place every time. (after I get the thing working.)
#when testing it would be a good idea to have the enemy be constant. 