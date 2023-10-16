def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

def num_points_per_game(player_name):
    player_points = {
        "Jarrett Allen": 16.1,
        "Darius Garland": 21.7,
        "Evan Mobley": 15.0,
        "Kevin Love": 13.6,
        "Isaac Okoro": 8.8,
        "Ricky Rubio": 13.1,
        "Bradley Beal": 23.2,
        "Kyle Kuzma": 17.1,
        "Kentavious Caldwell-Pope": 13.2,
        "Davis Bertans": 5.6,
        "Kristaps Porzingis": 22.1,
        "Rui Hachimura": 11.3,
    }
    
    if player_name in player_points:
        return player_points[player_name]
    else:
        return None 
    
def player_age(player_name):
    player_ages = {
        "Jarrett Allen": 24,
        "Darius Garland": 22,
        "Evan Mobley": 21,
        "Kevin Love": 34,
        "Isaac Okoro": 21,
        "Ricky Rubio": 31,
        "Bradley Beal": 29,
        "Kyle Kuzma": 27,
        "Kentavious Caldwell-Pope": 29,
        "Davis Bertans": 29,
        "Kristaps Porzingis": 27,
        "Rui Hachimura": 24,
    }
    if player_name in player_ages:
        return player_ages[player_name]
    else:
        return None

def team_colors(team_name):
    team_colors_dict = {
        "Cleveland Cavaliers": ["Wine", "Gold"],
        "Washington Wizards": ["Red", "White", "Navy Blue"],
    }
    if team_name in team_colors_dict:
        return team_colors_dict[team_name]
    else:
        return []
    
def team_names():
    team_names_list = ["Cleveland Cavaliers", "Washington Wizards"]
    return team_names_list

def player_numbers(team_name):
    team_player_numbers = {
        "Cleveland Cavaliers": [31, 10, 4, 0, 35, 99],
        "Washington Wizards": [3, 33, 1, 42, 6, 8],
    }
    if team_name in team_player_numbers:
        return team_player_numbers[team_name]
    else:
        return []
        
def player_stats(player_name):
    player_stats_dict = {
        "Jarrett Allen": {
            "name": "Jarrett Allen", "number": 31, "position": "Center",
            "points_per_game": 16.1, "rebounds_per_game": 10.8, "assists_per_game": 1.6,
            "steals_per_game": 0.8, "blocks_per_game": 1.3, "career_points": 3945,
            "age": 24, "height_inches": 82, "shoe_brand": "Nike",
        },
        "Darius Garland": {
            "name": "Darius Garland", "number": 10, "position": "Point Guard",
            "points_per_game": 21.7, "rebounds_per_game": 3.3, "assists_per_game": 8.6,
            "steals_per_game": 1.3, "blocks_per_game": 0.1, "career_points": 3142,
            "age": 22, "height_inches": 73, "shoe_brand": "Nike",
        },
        "Evan Mobley":{ 
            "name": "Evan Mobley", "number": 4, "position": "Center", 
            "points_per_game": 15.0, "rebounds_per_game": 8.3, "assists_per_game": 2.5, 
            "steals_per_game": 0.8, "blocks_per_game": 1.7, "career_points": 1034, 
            "age": 21, "height_inches": 83, "shoe_brand": "Adidas", 
        },
        "Kevin Love":{ 
            "name": "Kevin Love", "number": 0, "position": "Power Forward", 
            "points_per_game": 13.6, "rebounds_per_game": 7.2, "assists_per_game": 2.2, 
            "steals_per_game": 0.4, "blocks_per_game": 0.2, "career_points": 14305, 
            "age": 34, "height_inches": 80, "shoe_brand": "Nike", 
        },
       "Isaac Okoro":{ 
           "name": "Isaac Okoro", "number": 35, "position": "Small Forward", 
           "points_per_game": 8.8, "rebounds_per_game": 3.0, "assists_per_game": 1.8, 
           "steals_per_game": 0.8, "blocks_per_game": 0.3, "career_points": 1234, 
           "age": 21, "height_inches": 77, "shoe_brand": "Nike", 
        },
       "Ricky Rubio":{ 
           "name": "Ricky Rubio", "number": 99, "position": "Point Guard", 
           "points_per_game": 13.1, "rebounds_per_game": 4.1, "assists_per_game": 6.6, 
           "steals_per_game": 1.4, "blocks_per_game": 0.2, "career_points": 7399, 
           "age": 31, "height_inches": 74, "shoe_brand": "Adidas", 
        },
       "Bradley Beal":{ 
           "name": "Bradley Beal", "number": 3, "position": "Shooting Guard", 
           "points_per_game": 23.2, "rebounds_per_game": 4.7, "assists_per_game": 6.6, 
           "steals_per_game": 0.9, "blocks_per_game": 0.4, "career_points": 14231, 
           "age": 29, "height_inches": 76, "shoe_brand": "Nike", 
        },
       "Kyle Kuzma": { 
           "name": "Kyle Kuzma", "number": 33, "position": "Power Forward", 
           "points_per_game": 17.1, "rebounds_per_game": 8.5, "assists_per_game": 3.5, 
           "steals_per_game": 0.6, "blocks_per_game": 0.9, "career_points": 5336, 
           "age": 27, "height_inches": 81, "shoe_brand": "Puma", 
        },
       "Kentavious Caldwell-Pope": { 
           "name": "Kentavious Caldwell-Pope", "number": 1, "position": "Shooting Guard", 
           "points_per_game": 13.2, "rebounds_per_game": 3.4, "assists_per_game": 1.9, 
           "steals_per_game": 1.1, "blocks_per_game": 0.3, "career_points": 7911, 
           "age": 29, "height_inches": 77, "shoe_brand": "Nike", 
        },
       "Davis Bertans": { 
           "name": "Davis Bertans", "number": 42, "position": "Power Forward", 
           "points_per_game": 5.6, "rebounds_per_game": 2.1, "assists_per_game": 0.6, 
           "steals_per_game": 0.3, "blocks_per_game": 0.3, "career_points": 3165, 
           "age": 29, "height_inches": 82, "shoe_brand": "Nike", 
        },
       "Kristaps Porzingis": { 
           "name": "Kristaps Porzingis", "number": 6, "position": "Power Forward", 
           "points_per_game": 22.1, "rebounds_per_game": 8.8, "assists_per_game": 2.9, 
           "steals_per_game": 0.7, "blocks_per_game": 1.5, "career_points": 6371, 
           "age": 27, "height_inches": 87, "shoe_brand": "Adidas", 
        },
       "Rui Hachimura": { 
           "name": "Rui Hachimura", "number": 8, "position": "Power Forward", 
           "points_per_game": 11.3, "rebounds_per_game": 3.8, "assists_per_game": 1.1, 
           "steals_per_game": 0.5, "blocks_per_game": 0.2, "career_points": 1913, 
           "age": 24, "height_inches": 80, "shoe_brand": "Jordan", 
           }
    }

    if player_name in player_stats_dict:
        return player_stats_dict[player_name]
    else:
        return {}
    
def average_rebounds_by_shoe_brand():
    players = [
        {
            "name": "Jarrett Allen",
            "shoe_brand": "Nike",
            "rebounds_per_game": 10.8,
        },
        {
            "name": "Darius Garland",
            "shoe_brand": "Nike",
            "rebounds_per_game": 3.3,
        },
        {
            "name": "Evan Mobley",
            "shoe_brand": "Adidas",
            "rebounds_per_game": 8.30,
        },
        {
            "name": "Kevin Love",
            "shoe_brand": "Nike",
            "rebounds_per_game": 7.2,
        },
        {
            "name": "Isaac Okoro",
            "shoe_brand": "Nike",
            "rebounds_per_game": 3.0,
        },
         {
            "name": "Ricky Rubio",
            "shoe_brand": "Adidas",
            "rebounds_per_game": 4.1,
        },
         {
            "name": "Bradley Beal",
            "shoe_brand": "Nike",
            "rebounds_per_game": 4.7,
        },
           {
            "name": "Kyle Kuzma",
            "shoe_brand": "Puma",
            "rebounds_per_game": 8.5,
        },
           {
            "name": "Kentavious Caldwell-Pope",
            "shoe_brand": "Nike",
            "rebounds_per_game": 3.4,
        },
           {
            "name": "Davis Bertans",
            "shoe_brand": "Nike",
            "rebounds_per_game": 2.1,
        },
           {
            "name": "Kristaps Porzingis",
            "shoe_brand": "Adidas",
            "rebounds_per_game": 8.8,
        },
           {
            "name": "Rui Hachimura",
            "shoe_brand": "Jordan",
            "rebounds_per_game": 3.8,
        },
    ]
    shoe_brand_stats = {}

    for player in players:
        shoe_brand = player["shoe_brand"]
        rebounds = player["rebounds_per_game"]

        if shoe_brand in shoe_brand_stats:
            shoe_brand_stats[shoe_brand]["total_rebounds"] += rebounds
            shoe_brand_stats[shoe_brand]["count"] += 1
        else:
            shoe_brand_stats[shoe_brand] = {
                "total_rebounds": rebounds,
                "count": 1,
            }

    output_lines = []

    for brand, stats in shoe_brand_stats.items():
        average_rebounds = stats["total_rebounds"] / stats["count"]
        output_line = f"{brand}: {average_rebounds:.2f}"
        output_lines.append(output_line)

    output = "\n".join(output_lines)
    print(output)