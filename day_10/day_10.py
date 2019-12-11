import math

asteroid_map = []

with open('asteroid.dat') as asteroid_file:
    for row_number, row in enumerate(asteroid_file):
        for column_number, space in enumerate(row):
            if space == '#':
                asteroid_map.append((column_number, row_number))

max_visible = 0


def compute_angle(viewpoint, asteroid):
    if viewpoint[0] == asteroid[0]:
        if viewpoint[1] > asteroid[1]:
            return 0
        else:
            return math.pi
    else:
        return (math.atan2(asteroid[1] - viewpoint[1], asteroid[0] - viewpoint[0]) + math.pi / 2) % (2 * math.pi)


def compute_distance(from_asteroid, to_asteroid):
    return math.sqrt((from_asteroid[1] - to_asteroid[1])**2 + (from_asteroid[0] - to_asteroid[0])**2)


def compute_visible(viewpoint):
    visible_map = {}
    for asteroid in asteroid_map:
        if viewpoint == asteroid:
            continue
        angle = compute_angle(viewpoint, asteroid)
        distance = compute_distance(viewpoint, asteroid)

        if angle not in visible_map.keys() or distance < visible_map.get(angle)['distance']:
            visible_map[angle] = {'asteroid': asteroid, 'distance': distance}
    return visible_map


count = 0
best = None
vaporize_map = {}

for candidate in asteroid_map:
    visible = compute_visible(candidate)
    if len(visible) > count:
        best = candidate
        count = len(visible)
        vaporize_map = visible

print(best, count)
asteroid_keys = sorted(vaporize_map.keys())
print(vaporize_map.get(asteroid_keys[199])['asteroid'])
