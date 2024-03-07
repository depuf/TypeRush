import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typerush_project.settings')
import random
import django
django.setup()
from typerush.models import Player, Mode, Leaderboard, Game
from django.contrib.auth.models import User

def populate():
    # Create users
    users = []
    for i in range(1, 9):
        user = User.objects.create_user(username=f'user{i}', password=f'password{i}')
        users.append(user)

    # Create players
    players = []
    for i, user in enumerate(users, start=1):
        player = Player.objects.create(user=user, firstname=f'Player{i}', surname=f'User{i}', country='USA', total_races=5, average_speed=50)
        players.append(player)

    # Populate Leaderboard model
    easyleaderboard = Leaderboard.objects.create(title='Easy Leaderboard')
    mediumleaderboard = Leaderboard.objects.create(title='Medium Leaderboard')
    hardleaderboard = Leaderboard.objects.create(title='Hard Leaderboard')

    easyleaderboard.players.add(*players)
    mediumleaderboard.players.add(*players)
    hardleaderboard.players.add(*players)

    # Populate Mode model
    modes_data = [
        {'difficulty': 'Easy', 'races_played': 20, 'highscore': 50, 'leaderboard': easyleaderboard},
        {'difficulty': 'Medium', 'races_played': 17, 'highscore': 33, 'leaderboard': mediumleaderboard},
        {'difficulty': 'Hard', 'races_played': 15, 'highscore': 22, 'leaderboard': hardleaderboard}
    ]
    modes = []
    for mode_data in modes_data:
        mode = Mode.objects.create(**mode_data)
        modes.append(mode)

        # Populate Game model
        for player in players:
            for i in range(1, 6):  # Add 5 games for each mode and player
                score = random.randint(0,50) # Example score (decreasing for demonstration)
                Game.objects.create(mode=mode, user=player, score=score)

    print("Database populated successfully.")

# Main Method Execution
if __name__ == '__main__':
    print("Starting TypeRush Population Script...")
    populate()
