# Post Game Stats 🏈
# Codédex

# Task 1: Create Player Data
players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    {"name": "Josh Feldstein", "position": "Tight End", "jersey_number": 25, "yards_gained": 100, "touchdowns": 1},
    {"name": "Rashad Johnson", "position": "Defensive Back", "jersey_number": 35, "yards_gained": 75, "touchdowns": 0},
    {"name": "Derrick Henry", "position": "Running Back", "jersey_number": 22, "yards_gained": 200, "touchdowns": 2}
]

names = [players["name"] for players in players_data]
print("Players Names: ", names)

# Task 2: Analyze platyers positions

positions = [players["position"] for players in players_data]
print("Positions: ", positions)

# task 3: Update player Statistics

players_data[0]["yards_gained"] += 50
players_data[0]["touchdowns"] += 1

# Task 4 Calculate Average Stats

average_yards = sum(players_data["yards_gained"] for players_data in players_data) / len(players_data)
average_touchdowns = sum(players_data["touchdowns"] for players_data in players_data) / len(players_data)
print("Average Yards: ", average_yards)
print("Average Touchdowns: ", average_touchdowns)
