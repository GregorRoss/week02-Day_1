class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players =input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        player_exists = False
        if player in self.players:
            player_exists = True
        return(player_exists)
    
    def play_game(self, win):
        if win == True:
            self.points += 3
    
