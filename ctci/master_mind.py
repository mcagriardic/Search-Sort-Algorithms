"""
Cracking the Coding Interview
Play a game of mastermind:
Write a function which holds the answer to a mastermind game,
eg four pins with a combination of the colours/symbols Y, R, G, B (Yellow, red, green and blue)
The player should submit four pins with a combination of the four colours and
well as the suspected position of the colours.
If the player gets the position and the color right, then that's a full hit,
if they get the color right but not the position then that's a pseudo hit.
Return number of pseudo hits and actual hits based on a user's entry.
"""

from collections import defaultdict

def master_mind(guess):
    answer = ["Y", "B", "Y", "G"]

    # ac -> answer count
    ac = defaultdict(lambda: 0)
     
    # gc -> guess count
    gc = defaultdict(lambda: 0)

    # am -> actual match
    am = 0
    for a,g in zip(answer, guess):
        if a == g:
            am += 1
        ac[a] += 1
        gc[g] += 1

    # tm -> total match
    tm = 0
    # kg -> key guess
    for kg in gc:
        if gc[kg] >= ac[kg]:
            tm += ac[kg]
        elif gc[kg] < ac[kg]:
            tm += gc[kg]

    # pm -> pseudo match
    pm = tm - am

    return pm, am

# tcs -> test cases
tcs = ["BYYB", "BYYG", "YYYY", "RRRR"]
answers = [(2, 1), (2, 2), (0, 2), (0, 0)]
print([master_mind(t) == a for t,a in zip(tcs, answers)])

"""
>> [True, True, True, True]
"""