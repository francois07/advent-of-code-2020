input = [x for x in open('input.txt', 'r').read().splitlines()]

DIRECTIONS = ["N", "E", "S", "W"]


def parse_action(data):
    action = data[:1]
    value = int(data[1:])
    return (action, value)


def run_actions(data):
    actions = [parse_action(line) for line in data]
    current_position = {direction: 0 for direction in DIRECTIONS}
    facing_direction_idx = 1
    for action in actions:
        if action[0] not in "LRF":
            current_position[action[0]] += action[1]
        elif action[0] in "LR":
            degree = action[1] // 90
            if action[0] == "L":
                facing_direction_idx = (
                    facing_direction_idx-degree) % len(DIRECTIONS)
            elif action[0] == "R":
                facing_direction_idx = (
                    facing_direction_idx+degree) % len(DIRECTIONS)
        elif action[0] == "F":
            current_position[DIRECTIONS[facing_direction_idx]] += action[1]
    return current_position


def manhattan_distance(position):
    vertical = abs(position["N"] - position["S"])
    horizontal = abs(position["W"] - position["E"])
    return horizontal + vertical


end_position = run_actions(input)
print(manhattan_distance(end_position))
