def fuel(mass_of_component):
    return int(mass_of_component / 3) - 2


def fuel_for_component(mass_of_component_fuel):
    fuel_fuel = 0

    fuel_mass = fuel(mass_of_component_fuel)
    while fuel_mass >= 0:
        print('+'+str(fuel_mass))
        fuel_fuel += fuel_mass
        fuel_mass = fuel(fuel_mass)
    return fuel_fuel


list_of_module_masses = 'input.txt'
total_fuel = 0
total_fuel_fuel = 0
with open(list_of_module_masses) as masses:
    for line in masses:
        component_mass = int(line)
        component_fuel = fuel(component_mass)
        total_fuel += component_fuel

        component_fuel_fuel = fuel_for_component(component_fuel)
        total_fuel_fuel += component_fuel_fuel
        print(component_mass, component_fuel, component_fuel_fuel)


print(1969, fuel(1969), fuel_for_component(fuel(1969)))
print(total_fuel, total_fuel_fuel, total_fuel + total_fuel_fuel)
