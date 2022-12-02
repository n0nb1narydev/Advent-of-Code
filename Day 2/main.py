player_score = 0
opponent_score = 0

rock_points = 1
paper_points = 2
scissors_points = 3

win_points = 6
draw_points = 3
lose_points = 0

with open('input2.txt') as f:
    guide = f.readlines()

print(len(guide))

# X lose --- Y draw --- Z win
for ind, x in enumerate(guide):
    # opponent plays rock
    if x[0].upper() == 'A':
        if x[2].upper() == 'X':
            player_score += scissors_points + lose_points
        elif x[2].upper() == 'Y':
            player_score += rock_points + draw_points
        elif x[2].upper() == 'Z':
            player_score += paper_points + win_points
    # opponent plays Paper
    elif x[0].upper() == 'B':
        if x[2].upper() == 'X':
            player_score += rock_points + lose_points
        elif x[2].upper() == 'Y':
            player_score += paper_points + draw_points
        elif x[2].upper() == 'Z':
            player_score += scissors_points + win_points
    # opponent plays scissors
    elif x[0].upper() == 'C':
        if x[2].upper() == 'X':
            player_score += paper_points + lose_points
        elif x[2].upper() == 'Y':
            player_score += scissors_points + draw_points
        elif x[2].upper() == 'Z':
            player_score += rock_points + win_points

print(player_score)