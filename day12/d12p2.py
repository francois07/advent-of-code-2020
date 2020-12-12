input = [x for x in open('input.txt', 'r').read().splitlines()]

DIRECTIONS = ["N", "E", "S", "W"]


def parse_action(data):
    action = data[:1]
    value = int(data[1:])
    return (action, value)


def rotate_position(position, degree):
    n = degree // 90
    rotated = {DIRECTIONS[(i+n) % len(DIRECTIONS)]: position[DIRECTIONS[i]]
               for i in range(len(DIRECTIONS))}
    return rotated


def run_actions(data, waypoint_position):
    actions = [parse_action(line) for line in data]
    current_position = {direction: 0 for direction in DIRECTIONS}
    for action in actions:
        if action[0] not in "LRF":
            waypoint_position[action[0]] += action[1]
        elif action[0] in "LR":
            if action[0] == "L":
                waypoint_position = rotate_position(
                    waypoint_position, -action[1])
            elif action[0] == "R":
                waypoint_position = rotate_position(
                    waypoint_position, action[1])
        elif action[0] == "F":
            for position in waypoint_position:
                current_position[position] += action[1] * \
                    waypoint_position[position]
    return current_position


def manhattan_distance(position):
    vertical = abs(position["N"] - position["S"])
    horizontal = abs(position["W"] - position["E"])
    return horizontal + vertical


waypoint_position = {
    "N": 1,
    "E": 10,
    "S": 0,
    "W": 0
}
end_position = run_actions(input, waypoint_position)
print(end_position, manhattan_distance(end_position))
