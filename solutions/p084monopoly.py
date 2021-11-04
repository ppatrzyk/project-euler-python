import random
from collections import Counter, OrderedDict

ROUNDS = 1000000
SIDES = 4

squares = {i: None for i in range(40)}
for cc_index in (2, 17, 33):
    squares[cc_index] = 'CC'
for ch_index in (7, 22, 36):
    squares[ch_index] = 'CH'
squares[30] = 'jail'

def roll_advance(sides):
    die1 = random.choice(range(sides)) + 1
    die2 = random.choice(range(sides)) + 1
    is_double = (die1 == die2)
    result = die1 + die2
    return (result, is_double)

def cc_card(current_pos):
    choices = range(16)
    mapping = {i: None for i in choices}
    mapping[0] = 0 # Advance to GO
    mapping[1] = 10 # Go to JAIL
    draw = random.choice(choices)
    result = mapping[draw]
    if result is None:
        result = current_pos
    return result

def ch_card(current_pos):
    choices = range(16)
    mapping = {i: None for i in choices}
    railways = {
        7: 15,
        22: 25,
        36: 5
    }
    utilities = {
        7: 12,
        22: 28,
        36: 12
    }
    mapping[0] = 0 # Advance to GO
    mapping[1] = 10 # Go to JAIL
    mapping[2] = 11 # Go to C1
    mapping[3] = 24 # Go to E3
    mapping[4] = 39 # Go to H2
    mapping[5] = 5 # Go to R1
    mapping[6] = railways[current_pos] # Go to next R (railway company)
    mapping[7] = railways[current_pos] # Go to next R
    mapping[8] = utilities[current_pos] # Go to next U (utility company)
    mapping[9] = (current_pos-3) # Go back 3 squares.
    draw = random.choice(choices)
    result = mapping[draw]
    if result is None:
        result = current_pos
    return result

def simulate(rounds):
    consecutive = 0
    current_pos = 0
    pos_history = [current_pos, ]
    for _ in range(rounds):
        roll = roll_advance(SIDES)
        roll_amount = roll[0]
        roll_is_double = roll[1]
        if roll_is_double:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive == 3:
            consecutive = 0
            new_position = 10
        else:
            consecutive = 0
            new_position = (current_pos + roll_amount) % 40
            square_type = squares[new_position]
            if square_type is None:
                pass
            elif square_type == 'CC':
                new_position = cc_card(new_position)
            elif square_type == 'CH':
                new_position = ch_card(new_position)
            elif square_type == 'jail':
                new_position = 10
            else:
                # should never happen
                assert False
        pos_history.append(new_position)
        current_pos = new_position
    return pos_history




if __name__ == "__main__":
    sim = simulate(ROUNDS)
    sim_count = sorted(
        Counter(sim).items(),
        key=lambda e: -e[1]
    )
    print(sim_count[:3])