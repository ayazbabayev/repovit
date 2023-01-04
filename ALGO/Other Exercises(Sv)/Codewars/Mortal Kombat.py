
# declare_winner(Fighter("SubZero", 10, 2), Fighter("Scorpion", 5, 4), "SubZero") = > "Subzero"

# SubZero attacks Scorpion; Scorpion now has 3 health.
# Scorpion attacks SubZero; SubZero now has 6 health.
# SubZero attacks Scorpion; Scorpion now has 1 health.
# Scorpion attacks SubZero; SubZero now has 2 health.
# SubZero attacks Scorpion: Scorpion now has - 1 health and is dead.
# SubZero wins.

# def declare_winner(p1, health1, hit1, p2, health2, hit2, attacker):
#     while attacker is p1:
#         health2 = health2 - hit1
#         print(health2 - hit1)
#         health1 = health1 - hit2
#         print(health1 - hit2)
#         if health2 < 0:
#             break
#         print(p1+' wins!')
#         if health1 < 0:
#             break
#         print(p2+' wins!')
#
#     while attacker is p2:
#         health1 = health1 - hit2
#         print(health1 - hit2)
#         health2 = health2 - hit1
#         print(health2 - hit1)
#         if health1 < 0:
#             break
#         print(p2 + ' wins!')
#         if health2 < 0:
#             break
#         print(p1 + ' wins!')
#
#
# p1 = 'Subzero'
# health1 = 10    # 10
# hit1 = 2        # 2
#
# p2 = 'Scorpion'
# health2 = 5     # 5
# hit2 = 4        # 4
#
# attacker = 'Subzero'
#
# test_fight = declare_winner(p1, health1, hit1, p2, health2, hit2, attacker)
# print(test_fight)

#######################################################################################################
class Fighter:
    def __init__(self, name, health, hit):
        self.name = name
        self.health = health
        self.hit = hit

player_1 = Fighter('SubZero', 10, 2)
player_2 = Fighter('Scorpion', 5, 4)

def declare_winner(player_1, player_2, starter):
    player_lists = []
    if starter == 1:
        player_lists.extend([player_1, player_2])
    else:
        player_lists.extend([player_2, player_1])

    i = starter - 1