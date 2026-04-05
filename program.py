class PlayerData:
    index_counter = 0
    def __init__(self, name):
        #self.row_len = None
        self.name = name
        self.points = []
        self.index = self.index_counter
        PlayerData.index_counter += 1

    def get_points(self):
        return sum(self.points)

    def is_win(self):
        return self.get_points() >= win_numb

    def get_row_len(self):
        longest = len(self.name)
        for n in self.points:
            if len(str(n)) > longest:
                longest = len(str(n))
        # Berücksichtige auch die Länge der Summe
        if len(str(self.get_points())) > longest:
            longest = len(str(self.get_points()))
        return longest

    def __str__(self):
        return "Player no." + str(self.index + 1) + " : " + str(self.name) + " : currently " + str(self.get_points()) + " points"


win_numb = 10000
player_count = None
players = []
nunber_row_titel = "Round"
number_row_prefix = "No."
round_counter = 0
vertical_seperator = " | "



def goal_reached(player):
    print(r"""
        _  _____ _____ _____ _   _ _____ ___ ___  _   _
       / \|_   _|_   _| ____| \ | |_   _|_ _/ _ \| \ | |
      / _ \ | |   | | |  _| |  \| | | |  | | | | |  \| |
     / ___ \| |   | | | |___| |\  | | |  | | |_| | |\  |
    /_/   \_\_|   |_| |_____|_| \_| |_| |___\___/|_| \_|

    """)
    print(player)
    print("has reached", win_numb, "points." "If no one beats them in this round they will win!" if  player_count != player.index + 1 else "As they are the last player in this round they will win")


def get_valid_int_inp():
    """
    Endless loop, takes input returns as int if able to cast
    Oterwise asks for input again
    :return: input as int
    """
    while True:
        try:
            inp = input()
            if inp == "r":
                correction()
            else:
                return int(inp)
        except:
            print("Input invalid")

def create_list(amount):
    players = []
    for i in range(amount):
        while True:
            print("Please input name of player no.", i + 1)
            inp_name = input()
            if len(inp_name) == 0:
                print("Name can't have length 0")
            else:
                break
        players.append(PlayerData(inp_name))
    return players

def inp_player_count():
    while True:
        print("Please input amount of players")
        inp = get_valid_int_inp()
        if inp <= 0:
            print("Amount can't be 0 or negative")
        else:
            return inp


def correction():
    global players
    print("Please input player no. to change the points")
    inp_pla = None
    while True:
        try:
            inp_pla_raw = input()
            if inp_pla_raw == "exit":
                return
            inp_pla = int(inp_pla_raw)
            if inp_pla - 1 < len(players):
                break
            else:
                print("Player no. doesnt exist")
        except:
            print("Input invalid")
    print(inp_pla)
    print("Please input the round nr.")
    inp_round = None
    while True:
        try:
            inp_round_raw = input()
            if inp_round_raw == "exit":
                return
            inp_round = int(inp_round_raw)
            if inp_round <= len(players[inp_pla - 1].points):
                break
            else:
                print("Round no. doesnt exist")
        except:
            print("Input invalid")
    print(inp_round)
    print("Please input the correction")
    inp_corr = None
    while True:
        try:
            inp_corr_raw = input()
            if inp_corr_raw == "exit":
                return
            inp_corr = int(inp_corr_raw)
            if inp_corr > 0 and inp_corr % 50 != 0:
                print("Input must be devidable by 50 and positive")
            else:
                break
        except:
            print("Input invalid")
    print(inp_corr)
    players[inp_pla - 1].points[inp_round - 1] = inp_corr
    print("Correction done, please input the points, as previously asked")


def get_points_input():
    while True:
        inp = get_valid_int_inp()
        if inp < 0:
            print("Number must be positive")
        elif inp % 50 != 0:
            print("Number must be devidable by 50")
        else:
            return inp

def sort_players(players_over):
    return sorted(players_over, reverse=True, key=lambda x: x.points)

def get_number_row_len():
    row_len = len(nunber_row_titel)
    row_len_with_number = len(number_row_prefix) + len(str(round_counter))
    if row_len_with_number > row_len:
        return row_len_with_number
    return row_len

def get_missing_spaces(length, str_over):
    ret = ""
    for i in range(length - len(str(str_over))):
        ret += " "
    return  ret

def return_first_line(number_row_len, player_row_len):
    ret = ""
    ret += nunber_row_titel
    ret += get_missing_spaces(number_row_len, nunber_row_titel)
    counter = 0
    for n in players:
        ret += vertical_seperator
        ret += n.name
        ret += get_missing_spaces(player_row_len[counter], n.name)
        counter += 1
    return ret


def return_points_row(number_row_len, player_row_len, current_round):
    ret = ""
    ret += number_row_prefix + str(current_round)
    ret += get_missing_spaces(number_row_len, number_row_prefix + str(current_round))
    for i in range(len(players)):
        ret += vertical_seperator
        if len(players[i].points) >= current_round:
            ret += str(players[i].points[current_round - 1])
            ret += get_missing_spaces(player_row_len[i], str(players[i].points[current_round - 1]))
        else:
            ret += get_missing_spaces(player_row_len[i], "")
    return ret


def return_last_row(number_row_len, player_row_len):
    ret = ""
    ret += "Sum"
    ret += get_missing_spaces(number_row_len, "Sum")
    for n in range(len(players)):
        ret += vertical_seperator
        ret += str(players[n].get_points())
        ret += get_missing_spaces(player_row_len[n], players[n].get_points())
    return ret


def round_print():
    global players, round_counter
    number_row_len = get_number_row_len()
    player_row_len = []
    for n in players:
        player_row_len.append(n.get_row_len())

    to_print = ""

    for i in range(round_counter + 1):
        if i == 0:
            to_print += return_first_line(number_row_len, player_row_len)
        else:
            to_print += "\n"
            for _ in range(sum(player_row_len) + number_row_len + len(player_row_len) * 3):
                if i == 1:
                    to_print += "="
                else:
                    to_print += "-"
            to_print += "\n"
            to_print += return_points_row(number_row_len, player_row_len, i)

    to_print += "\n"
    for i in range(sum(player_row_len) + number_row_len + len(player_row_len) * 3):
        to_print += "="

    to_print += "\n"
    to_print += str(return_last_row(number_row_len, player_row_len))

    print(to_print)


def run_game():
    global players, round_counter
    cont = True
    game_won = False
    while cont:
        round_counter += 1
        for n in players:
            print()
            round_print()
            print("\nPlease input the points from ", n, ". Or \"r\" to correct a previous input")
            n.points.append(get_points_input())
            if sum(n.points) >= win_numb:
                goal_reached(n)
                game_won = True
        if game_won and input("Finish game? type \"y\"") == "y":
            break
        else:
            game_won = False


def finish():
    players_sorted = sorted(players, reverse = True, key=lambda x: x.points)
    print("Here the whole list:")
    round_print()
    print("here the players in order")
    for n in players_sorted:
        print(n)



def initialize_game():
    global player_count, players
    player_count = inp_player_count()
    players = create_list(player_count)
    run_game()
    finish()


if __name__ == '__main__':
    initialize_game()
