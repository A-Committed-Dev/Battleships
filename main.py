
def create_ships():
    ships = []
    ships.append(["O","O",])
    # ships.append(["O", "O","O",])
    # ships.append(["O", "O", "O", "O",])
    return ships

def create_battlefield():
    battlefield =[]

    for i in range(0,6):
        battlefield.append([" ", " ", " ", " ", " ", " "])
    return battlefield


def print_battlefield(battlefield):
    try:
        n = 1
        for i in range(0, len(battlefield)):
            print(n, battlefield[n - 1])
            n +=1
        print("    a    b    c    d    e    f")
    except:
        pass


def place_ship(battlefield, ship, pos):
    ship_length = len(ship)
    try:
        if pos[2] == 1:
            for i in range(0, ship_length):
                if battlefield[pos[0]+i][pos[1]] == "O":
                    return "occupied"

                else:
                    battlefield[pos[0]+i][pos[1]] = ship[i]
            return battlefield
        else:
            for i in range(0, ship_length):
                if battlefield[pos[0]][pos[1]+i] == "O":
                    return "occupied"

                else:
                    battlefield[pos[0]][pos[1]+i] = ship[i]
            return battlefield
    except:
        return "Ship to big to fit"





def read_input(input):
    try:
        data = input.split(",")
        n = 0
        for z in ["a", "b", "c", "d", "e", "f"]:
            if data[1] == z:
                data[1] = n
            n+=1

        for i in range(0, len(data)):
            data[i] = int(data[i])
        data[0] = data[0]-1
        return data
    except:
        return "user is dumb"


def setup_ships(battlefield, ships):
    for i in range(0, len(ships)):
        print_battlefield(battlefield)
        resault = place_ship(battlefield, ships[i], read_input(input("Place ship | example | 1, a, 0    ->")))
        if resault == "occupied" or resault == "Ship to big to fit":
            print(resault+ ", try again")
            battlefield = create_battlefield()
            return setup_ships(battlefield, ships)

    return battlefield

def check_hit(battlefield,hit_battlefield, pos):
    if battlefield[pos[0]][pos[1]] == "O":
        print("~HIT~")
        battlefield[pos[0]][pos[1]] = "Ø"
        hit_battlefield[pos[0]][pos[1]] = "Ø"
    else:
        print("~MISS~")
        hit_battlefield[pos[0]][pos[1]] = "~"

def win_check(battlefield):
    for i in battlefield:
        for x in i:
            if x == "O":
                return False
    return True

def setup_game():
    ships = create_ships()

    print("Player one - Place your ships")
    P1_battlefield = create_battlefield()
    P1_hit_battlefield = create_battlefield()
    P1_battlefield = setup_ships(P1_battlefield, ships)
    print_battlefield(P1_battlefield)

    print("Player two - Place your ships")
    P2_battlefield = create_battlefield()
    P2_hit_battlefield = create_battlefield()
    P2_battlefield = setup_ships(P2_battlefield, ships)
    print_battlefield(P2_battlefield)
    return P1_battlefield, P1_hit_battlefield, P2_battlefield, P2_hit_battlefield





def game_loop(P1_battlefield, P1_hit_battlefield, P2_battlefield, P2_hit_battlefield):
    loop = True
    while (loop):
        print("~ Player one ~")
        print_battlefield(P1_hit_battlefield)
        check_hit(P2_battlefield, P1_hit_battlefield, read_input(input("Pick a point to hit | example | 1,a ->")))

        print("~ Player two ~")
        print_battlefield(P2_hit_battlefield)
        check_hit(P1_battlefield, P2_hit_battlefield, read_input(input("Pick a point to hit | example | 1,a ->")))

        if win_check(P1_battlefield) or win_check(P2_battlefield):
            print("Game Over")
            if win_check(P1_battlefield) and win_check(P2_battlefield):
                print("Impossible, both fleets where decimated")
            elif win_check(P2_battlefield):
                print("Player one Wins")
                print("You decimated player two's fleet ")
                print_battlefield(P2_battlefield)
            elif win_check(P1_battlefield):
                print("Player two Wins")
                print("You decimated player ones fleet ")
                print_battlefield(P1_battlefield)
            loop = False


setup = setup_game()
game_loop(setup[0], setup[1], setup[2], setup[3])