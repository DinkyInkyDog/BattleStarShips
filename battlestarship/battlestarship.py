

#don't get rid of that.\/ I really need those letters.
letters = "abcdefghi"
#there will be two boards. One for the player and one for the enemy that print seperate and hold their own info
class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    bottom = "_________________________________________________________"
    user_rows = [row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i]
    #I need a seperate board for each of the different versions that will happen.
    #so this next one will be the enemy board view
    e_top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    e_row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_bottom = "_________________________________________________________"
    enemy_rows = [e_row_a, e_row_b, e_row_c, e_row_d, e_row_e, e_row_f, e_row_g, e_row_h, e_row_i]
    def __init__(self, enemy = False):
        self.fleet = {}
        self.enemy = enemy
        self.ships = []
#That list in ships is for the attack function to easily find the ships that are included in the board.
# I didn't want to mess with the fleet because a bunch of functions use that and I don't want to mess them up.

    def display(self):
        if self.enemy == False:
            print(self.top)
            for row in self.user_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.bottom)
        #tested and it work!! ^ 
        #for now I have the enemy one displaying the same but that won't be the case moving forward.
        if self.enemy == True:
            print(self.e_top)
            for row in self.enemy_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.e_bottom) 

    def mark_board(self, ship, list=letters):
        if ship.verticle == True:
            self.ships.append(ship)
            self.fleet[ship] = [item for sublist in ship.location.items() for item in sublist]
            index = 0
            row_letter = " "
            
            for letter in letters:
                if letters[index] in ship.location.keys():
                    row_letter = letters[index]
                    break
                else:
                    index += 1
            
            numbers_list = [value for sublist in ship.location.values() for value in sublist]
            
            if self.enemy == False:
                i = letters.find(row_letter)
                row = self.user_rows[i]
                index_3 = 0
                for number in range(0, len(numbers_list)):
                    row.pop(numbers_list[index_3])
                    row.insert(numbers_list[index_3], "  o  ")
                    print(row)
                    index_3 += 1
                #print(self.user_rows[i])
            #self.display()
                
                
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
                row.insert(c, "  ,  ")
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
               
            
                    


       
       
player = Board()
enemy = Board(enemy=True)

def find_index(letter, list=letters):
    index = list.index(letter)
    return index

class Ship:
    verticle = True
    alive = True
    def __init__(self, size, rank = "(A)", status=True):
        self.location = {}
        self.size = size
        #The initialized ship is friendly by default, so when making the enemy ships change to false.
        self.friendly = status
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank
        self.health = size
    def flip(self):
        if self.verticle == True:
            self.verticle = False
        else:
            self.verticle = True

    def assign_ship(self, letter, number, up = False, list=letters):
        if self.verticle == True:
            if self.size + number > 10:
                print("------------------Failed to asign----------------------")
                print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                return False
            else:
                add = 0
                for mark in range(0, self.size):
                    if letter not in self.location:
                        self.location[letter] = [number]
                        add += 1
                        continue
                    self.location[letter].append(number + add)
                    add += 1
        else:
            if up == False:
                index = find_index(letter)
                if index + self.size > len(letters):
                    print("------------------Failed to asign----------------------")
                    print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                    return False
                else:
                    for mark in range(0, self.size):
                        self.location[letters[index]] = number
                        index += 1
            else:
                index = find_index(letter)
                if index - self.size < 0:
                    print("------------------Failed to asign----------------------")
                    print("location invalid for {ship}: can't place ship off the board.".format(ship=self.name))
                    return False
                else:
                    for mark in range(0, self.size):
                        self.location[letters[index]] = number
                        index -= 1
    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def __repr__(self):
        return self.name

#player.display()
#enemy.display()

testship_1 = Ship(3)
#testship_1.flip()
enemytest_ship_1 = Ship(2)
enemytest_ship_1.health = 1

enemytest_ship_2 = Ship(4)
enemytest_ship_2.flip()
enemytest_ship_3 = Ship(3)

testship_1.assign_ship("a", 4)
enemytest_ship_1.assign_ship("d", 6, True)
enemytest_ship_2.assign_ship("a", 3)
enemytest_ship_3.assign_ship("b", 6)
#player.mark_board(testship_1)
#print(player.fleet)
enemy.mark_board(enemytest_ship_1)
enemy.mark_board(enemytest_ship_2)
enemy.mark_board(enemytest_ship_3)
#print(enemytest_ship_1.location)


player.attack("d", 6, enemy)