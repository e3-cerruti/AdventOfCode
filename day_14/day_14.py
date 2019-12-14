from collections import defaultdict
from operator import methodcaller

formula = 1046184
REACTION_FILE = 'input.dat'


def read_reaction_file(file_name):
    formula = {}
    with open(file_name) as reaction_file:
        for reaction in reaction_file:
            inputs, output = reaction.strip().split(' => ')
            (quantity, chemical) = output.split(' ')
            parts = list(map(methodcaller('split', ' '), inputs.split(', ')))
            formula[chemical] = {'quantity': quantity, 'inputs': parts}
    return formula


def use_inventory(ingredient, inventory, needed):
    if ingredient in inventory.keys():
        on_hand = inventory.get(ingredient)
        if on_hand <= needed:
            del inventory[ingredient]
            return on_hand
        else:
            inventory[ingredient] = on_hand - needed
            return needed
    else:
        return 0


def store_excess(inventory, ingredient, overage):
    if overage:
        on_hand = inventory.get(ingredient) if ingredient in inventory.keys() else 0
        inventory[ingredient] = on_hand + overage


def process(formula, chemical='FUEL', quantity=1, inventory=defaultdict(list)):
    # print('Need: ', quantity, ' of ', chemical)
    # print(inventory)
    # print()
    if chemical == 'ORE':
        return quantity
    else:
        recipe = formula[chemical]
        makes = int(recipe['quantity'])
        number_of_blocks = quantity // makes
        if quantity % makes != 0:
            number_of_blocks += 1

        # print('Requires ', recipe, ' makes ', makes, ' blocks ', number_of_blocks)
        ore = 0
        for inputs in recipe['inputs']:
            recipe_needs = int(inputs[0]) * number_of_blocks
            recipe_needs -= use_inventory(inputs[1], inventory, recipe_needs)
            ore += process(formula, inputs[1], recipe_needs, inventory)

        store_excess(inventory, chemical, number_of_blocks * makes - quantity)
        return ore

master_formula = read_reaction_file(REACTION_FILE)
ore_on_board = 1000000000000
inventory=defaultdict(list)
total_fuel = 0
while ore_on_board > formula:
    fuel_amount = ore_on_board // formula
    ore_on_board -= process(master_formula, quantity=fuel_amount, inventory=inventory)
    if ore_on_board > 0:
        total_fuel += fuel_amount
    print(total_fuel, fuel_amount, ore_on_board)

# print(quantity_of_ore)
print(total_fuel)