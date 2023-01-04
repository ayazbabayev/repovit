# Our football team has finished the championship.
# Our team's match results are recorded in a collection of strings.
# Each match is represented by a string in the format "x:y",
# where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:
#
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the no of points
# our team (x) got in the championship by the rules given above.
# Notes:

# our team always plays 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

# def team_scores(match_dict):
#     match_dict = {0:1,1:0,2:1,3:4,4:4,3:2,2:2,1:1,4:1,3:0}
#
#     for key in match_dict.keys():
#         return sum(match_dict.keys(x))

def points(x):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>=res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

games = ['1:0','1:0','1:2','1:4','1:4','1:2','1:2','1:3','1:0','1:0']
result = points(games)
print(result)


def dict(x):
    return ''.join(d.keys())
d = {'key1': 1, 'key2': 14, 'key3': 47}
result = dict(d)
print(result)