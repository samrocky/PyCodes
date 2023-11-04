import random

class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Player(Human):
    def __init__(self, name, age, height, xp):
        super().__init__(name, age, height)
        self.xp = xp

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.mean_age = 0
        self.mean_height = 0
        self.mean_xp = 0
    def add_player(self, player):
        self.players.append(player)
        self.mean_age = sum([s.age for s in self.players]) / len(self.players)
        self.mean_height = sum([s.height for s in self.players]) / len(self.players)
        self.mean_xp = sum([s.xp for s in self.players]) / len(self.players)

players = [('hossein', 22, 180, 50),("maziar", 20, 176, 45),("akbar", 21, 175, 48)
               ,("nima", 18, 190, 60),('mehdi', 23, 182, 56),('farhad', 19, 182, 45)
               ,("mohammad", 21, 185, 45),("khashayar", 21, 179, 46),("milad", 19, 185, 52)
               ,("mostafa", 21, 175, 60),("amin", 19, 178, 58),("saead", 23, 180, 49)
               ,("pouya", 24, 175, 38),("pouria", 19, 174, 39),("reza", 19, 178, 46)
               ,("ali", 25, 180, 52),("behzad", 17, 169, 69),("soheil", 19, 176, 64)
               ,("behrooz", 19, 175, 41),("shahrooz", 24, 175, 51),("saman", 25, 165, 65),("mohsaen", 18, 180, 80)]

random.shuffle(players)

team_a = Team("A")

for i in players[:11]:
    team_a.add_player(Player(i[0], i[1], i[2], i[3]))

team_b = Team("B")

for i in players[11:]:
    team_b.add_player(Player(i[0], i[1], i[2], i[3]))

for i in team_a.players:
    print(i.name, "Team A")

#print("Height mean of team A is {}, Age mean is {} and Experience mean is {}".format(team_a.mean_height, team_a.mean_age, team_a.mean_xp))

for i in team_b.players:
    print(i.name, "Team B")

#print("Height mean of team B is {}, Age mean is {} and Experience mean is {}".format(team_b.mean_height, team_b.mean_age, team_b.mean_xp))