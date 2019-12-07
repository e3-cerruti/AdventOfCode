orbit_list = {}


def increment_child_depth(orbit):
    orbit_list[orbit]['depth'] = orbit_list[orbit_list[orbit].get('parent')].get('depth') + 1
    if 'children' in orbit_list[orbit].keys():
        for child in orbit_list[orbit]['children']:
            increment_child_depth(child)


def count_orbits(base):
    depth = orbit_list[base].get('depth')
    count = depth
    children = orbit_list[base].get('children')
    if children:
        for child in children:
            count += count_orbits(child)
    return count


def transfer(body, delta):
    if delta <= 0:
        return
    current_depth = orbit_list[body]['depth']
    parent = orbit_list[body].get('parent')
    grandparent = orbit_list[parent].get('parent')
    orbit_list[parent].setdefault('children', []).remove(body)
    orbit_list[grandparent].setdefault('children', []).append(body)
    orbit_list[body]['depth'] = current_depth - 1
    orbit_list[body]['parent'] = grandparent
    transfer(body, delta - 1)
    return


with open('Day06.dat') as orbit_file:
    orbits = [orbit.rstrip().split(')') for orbit in orbit_file]

for orbit in orbits:
    if orbit[0] in orbit_list.keys() and orbit[1] in orbit_list.keys():
        orbit_list[orbit[0]].setdefault('children', []).append(orbit[1])
        orbit_list[orbit[1]].update({'parent': orbit[0]})
        increment_child_depth(orbit[1])
    elif orbit[1] in orbit_list.keys():
        orbit_list[orbit[0]] = {}
        orbit_list[orbit[0]].update({'depth': orbit_list[orbit[1]]['depth']})
        orbit_list[orbit[0]].update({'children': [orbit[1]]})
        orbit_list[orbit[1]].update({'parent': orbit[0]})
        increment_child_depth(orbit[1])
    elif orbit[0] in orbit_list.keys():
        orbit_list[orbit[1]] = {}
        orbit_list[orbit[1]].update({'parent': orbit[0]})
        orbit_list[orbit[1]].update({'depth': orbit_list[orbit[0]]['depth'] + 1})
        orbit_list[orbit[0]].setdefault('children', []).append(orbit[1])
    else:
        orbit_list[orbit[0]] = {}
        orbit_list[orbit[1]] = {}
        orbit_list[orbit[0]]['children'] = [orbit[1]]
        orbit_list[orbit[0]]['depth'] = 0
        orbit_list[orbit[1]]['depth'] = 1
        orbit_list[orbit[1]].update({'parent': orbit[0]})

print("Total orbits:",count_orbits("COM"))

transfers = 0
you = 'YOU'
santa = 'SAN'

distance = orbit_list[you].get('depth') - orbit_list[santa].get('depth')
transfers += abs(distance)

if distance > 0:
    transfer(you, distance)
else:
    transfer(santa, abs(distance))

while orbit_list[you].get('parent') != orbit_list[santa].get('parent'):
    transfer(you, 1)
    transfer(santa, 1)
    transfers += 2

print("Transfers required to reach Santa:",transfers)
