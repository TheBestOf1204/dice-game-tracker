win_numb = 10000
class PlayerData:
    index_counter = 0
    def __init__(self, name):
        self.row_len = None
        self.name = name
        self.points = []
        self.index = self.index_counter
        PlayerData.index_counter += 1

    def get_points(self):
        return sum(self.points)

    def is_win(self):
        return self.get_points() >= win_numb

    def update_row_len(self):
        if round_counter == 1:
            self.row_len = len(self.name)
        else:
            if len(str(self.points[len(self.points) - 1])) > len(self.name):
                self.row_len = len(str(self.points[len(self.points) - 1]))
            else:
                self.row_len = len(self.name)

    def blablabla(self):

    def __str__(self):
        return "Player no." + str(self.index + 1) + " : " + str(self.name) + " : currently " + str(self.get_points()) + " points"


while True:
    print("input player number:")
    inp_players = input()
    try:
        inp_int = int(inp_players)
        break
    except:
        print("input invalid")
    

players = []
counter = 0
for n in range(inp_int):
    while True:
        counter += 1
        print("Please input name of player no.", counter)
        inp_name = input()
        if len(inp_name) == 0:
            print("Name can't have length 0")
        else:
            break
    players.append(PlayerData(inp_name))


def print_blank(times):
    for i in range(times):
        print()

#print_blank(8)

def print_all(to_print):
    for current in to_print:
        print(current)


def get_input():
    while True:
        inp = input()
        try:
            inp_int = int(inp)
            if inp_int == 0 or inp_int % 50 == 0 and inp_int > 0:
                return inp_int
            else:
                print("number is invalid; must be positive and dividable by 50")
        except:
            print("input invalid")

def get_players_sorted():
    players_sorted = sorted(players, reverse = True, key=lambda x: x.points)
    return players_sorted

def round_print(n):
    print_list()
    print("\n\nPlease enter the score of")
    print(n)

def print_list():
    round_prefix = "No."
    no_row_titel = "Round"
    output = ""
    last_str = "Sum"

    no_row_len = len(no_row_titel)
    if len(round_prefix) + len(str(round_counter)) > len(no_row_titel):
        no_row_len = len(round_prefix) + len(str(round_counter))

    for n in players:
        n.update_row_len()

    for i in range(round_counter):
        line_len = no_row_len
        for pl in players:
            line_len += 3 + pl.row_len
        for z in range(line_len):
            output += "-"
        output += "\n"
        if i == 0:
            output += no_row_titel
            for y in range(no_row_len - len(no_row_titel)):
                output += " "

            for n in players:
                output += " | " + n.name
                for y in range(n.row_len - len(n.name)):
                    output += " "
        else:
            output += round_prefix + str(i)
            for y in range(no_row_len - len(round_prefix) - len(str(i))):
                output += " "
            for n in players:
                output += " | " + str(n.points[i-1])
                for y in range(n.row_len - len(str(n.points[i-1]))):
                    output += " "
        output += "\n"

    line_len = no_row_len
    for pl in players:
        line_len += 3 + pl.row_len
    for z in range(line_len):
        output += "="
    output += "\n"

    output += last_str
    for y in range(no_row_len - len(last_str)):
        output += " "
    for n in players:
        output += " | " + str(n.get_points())
        for y in range(n.row_len - len(str(n.get_points()))):
            output += " "


    print(output)


def goal_reached():
    global cont
    cont = False
    print(r"""
        _  _____ _____ _____ _   _ _____ ___ ___  _   _
       / \|_   _|_   _| ____| \ | |_   _|_ _/ _ \| \ | |
      / _ \ | |   | | |  _| |  \| | | |  | | | | |  \| |
     / ___ \| |   | | | |___| |\  | | |  | | |_| | |\  |
    /_/   \_\_|   |_| |_____|_| \_| |_| |___\___/|_| \_|

    """)
    print(n)
    print("has reached", win_numb, "points." "If no one beats them in this round they will win!" if len(
        players) != n.index + 1 else "As they are the last player in this round they will win")
    #print_blank(4)

round_counter = 1
cont = True
while cont:
    for n in players:
        if round_counter != 0:
            round_print(n)
        inp = get_input()
        n.points.append(inp)
        #print_blank(16)
        if n.is_win():
            goal_reached()
    round_counter += 1

players_sorted = get_players_sorted()
print("----====----")
print("Winner:")
print(players_sorted[0])
print("----====----")
for n in players_sorted:
    print(n)

