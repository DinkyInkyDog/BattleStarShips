import os

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
#This is the one I shall continue to work on.
run_game = True
#don't get rid of that.\/ I really need those letters.
letters = "abcdefghij"
scout = """     ___
 ___/   \___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    /   \\
    /   \\
    /   \ """
fighter = """ o            o
  \          /
   \        /
    :-'""'-:
 .-'  ____  `-.
( (  (_()_)  ) )
 `-.   ^^   .-'
    `._==_.'
     __)(___ """
cargo = """ooo
        / : \\
       / o0o \\
 _____"~~~~~~~"_____
 \+###|U * * U|###+/
  \...!(.>..<)!.../
   ^^^^o|   |o^^^^
+=====}:^^^^^:{=====+#
.____  .|!!!|.  ____.
|#####:/" " "\:#####|
|#####=|  O  |=#####|
|#####>\_____/<#####|
 ^^^^^   | |   ^^^^^
         o o """
mothership = """           \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._""  \ _,="=._ /  ""_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\\
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\\
/'       )                  _                  (       `\\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \\
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \\
      /,'             | | | | | | |             `,\\
     /'               ` | | | | | '               `\\
                        ` | | | '
                          ` | ' """
class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10   |"""

    bottom = "_________________________________________________________"

    def __init__(self, name):
        self.fleet = []
        self.miss = []
        self.name = name
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

    def check_for_defeat(self):
        defeated = False
        dead_ships = 0
        for ship in self.fleet:
            if ship.alive == False:
                dead_ships += 1
        if dead_ships == 5:
            defeated = True
        return defeated

    def attack(self, r, c, board_being_attacked, letters=letters, run_game=run_game):
        target_hit = False
        for ship in board_being_attacked.fleet:
            if [r, c] in ship.location:
                target_hit = True
                ship.location.remove([r, c])
                ship.hit.append([r, c])
                print("You Hit!!")
                if len(ship.location) == 0:
                    ship.alive = False
                    if board_being_attacked.check_for_defeat() == True:
                        print("{player} wins!!".format(player=self.name))
                        run_game = False
                        break
                break
        if target_hit == False:
            self.miss.append([r, c])
            print("You missed...")
            
            

# player = Board()
# enemy = Board()


class Ship:
    
    alive = True
    def __init__(self, size, rank = "(A)"):
        self.location = []
        self.hit = []
        self.size = size
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank
#when setting up the fleets, each player gets 5 ships. x2 fighter jets and 1 of each of the others.
#be sure to label the two fighter jets, (A) and (B)
    def assign_ship(self, letter, number, board, verticle = True, up = False, left = False, list=letters):
        board.fleet.append(self)
        size_sub = self.size - 1
        self.verticle = verticle
        starting_letter_index = letters.index(letter)
        if self.verticle == True and up == False:
            if size_sub + starting_letter_index > 10:
                print("------------------Failed to assign----------------------")
                print("location invalid for {ship}: {row}{num} going down takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index += 1
        if self.verticle == True and up == True:
            if size_sub - starting_letter_index < 0:
                print("------------------Failed to assign----------------------")
                print("location invalid for {ship}: {row}{num} going up takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index -= 1

        if self.verticle == False:
            if left == True:
                if int(number) - size_sub <= 0:
                    print("------------------Failed to assign----------------------")
                    print("location invalid for {ship}: {row}{num} going left takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                    return False
                else:
                    num = number
                    for location in range(0, self.size):
                        self.location.append([letter, num])
                        num -= 1
            else:
                if int(number) + size_sub > 10:
                    print("------------------Failed to assign----------------------")
                    print("location invalid for {ship}: {row}{num} going right takes the ship off the board.".format(ship=self.name))
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


# ship_1 = Ship(4, "(A)")
# ship_1.assign_ship("b", 6, player, False, False, True)
# print(player.fleet)
section = "-----------------------------------------------------------------------------------------------------------------"
# enemy.attack('b', 4, player)
print(""" 
 ________             __       __      __ _                _______  _                ___    _             
(    _   \           (   )__ (    )_ (_    )              (    __ \( )_             (  _  \( )    _       
|  (__)   ) _ _ _____|    __)       _)|   |     ____       |  (__(_)  _)  _ _ _ __  | (__(_) |__ (_) __ __  
|    _  (  /   __    )   |   |    |   |   |   /  ____ \     \__  \ | |  / _  )  __)  \___ \|  _  \ |   __  \ 
|  (__)  )|   (__|  |    |__ |    |__ |   |__(  ______/   ( )__)  || |_( (_| | |    ( )__) | | | | |  (__)  )
(_______/  \__ ______)\_____)\_______)_______)\_______)    \______)\___)\__ _)_)     \_____)_) (_)_)     __/ 
                                                                                                    |  |    
                                                                                                    (___)
-----------------------------------------------------------------------------------------------------------------""")
print("Welcome to the squad commander. This is a two player game where one person has access to this screen and passes to the other player when prompted.")
print("Let's get started!")
print(section)

p1_name = input("Player One, what is your name? ex. Lauren          ")
p1_board = Board(p1_name)
p2_name = input("Player Two, what is your name? ex. Mark            ")
p2_board = Board(p2_name)
print("""
              ----Players set----
        phase one: player identification
                    COMPLETE
    
    
      Begin phase two: fleet assignments""")
swap = input("""{p1} prepare to assign your ships. {p2} do not look.
             press enter when ready""".format(p1=p1_name, p2=p2_name))
clear()
p1_scout = Ship(2)
p1_fighter_a = Ship(3)
p1_fighter_b = Ship(3, "(B)")
p1_cargo = Ship(4)
p1_mother = Ship(5)
p1_ships = [p1_scout, p1_fighter_a, p1_fighter_b, p1_cargo, p1_mother]
def pl_ship_assignments(player, ships_list):
    for ship in ships_list:
        placed_ship = False
        index = 0
        print("""                   ---{p}---
        Assign the {type} which takes up {size} spaces on the map.
            """.format(p=player.name, type=ship.name, size=ship.size))
        player.display()
        row = input("choose a starting point. choose a row (the letter must be lower case. ex. b )     ")
        column = int(input("now a column.     "))
        v_q = input("Will the ship be verticle? yes or no.      ")
        verticle = True
        up = False
        left = False
        if v_q == "yes" or v_q == "Yes" or v_q == "y":
            verticle = True
        if v_q == "no" or v_q == "No" or v_q == "n":
            verticle = False
        
        if verticle == True:
            up_q = input("Do you want the ship going up from the starting point or down?     ")
            if up_q == "up":
                up = True
            else:
                up = False
        else:
            left_q = input("Do you want the ship going left or right from the starting point?    ")
            if left_q == "left" or "l":
                left = True
            else:
                left = False
        ships_list[index].assign_ship(row, column, player, verticle, up, left)
        #I want the loop to start over if they try and place a ship where it can't go. 
        if ships_list[index].assign_ship(row, column, player, verticle, up, left) == False:
            break
        p1_board.display()
        index += 1
        pause = input("press enter to continue")



pl_ship_assignments(p1_board, p1_ships)