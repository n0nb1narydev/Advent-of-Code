# make a container dictionary with the stacks
# make a list of lists with the [qty, start, end] for each row

with open('day5.txt') as f:
    data = f.readlines()

directions_raw = data[10::]
directions_clean = []


cargo = {1: ['H', 'T', 'Z', 'D'], 
        2:['Q', 'R', 'W', 'T', 'G', 'C', 'S'], 
        3:['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'], 
        4:['L', 'C', 'N', 'F', 'H', 'Z'], 
        5:['G', 'L', 'F', 'Q', 'S'], 
        6:['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'], 
        7:['Z', 'F', 'J'], 
        8:['D', 'L', 'V', 'Z', 'R', 'H', 'Q'], 
        9:['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']}

test_cargo = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}
direction_test = [[1, 2, 1],[3, 1, 3], [2, 2, 1], [1, 1, 2]]

# print(directions_raw)
for row in directions_raw:
    direction = []
    row = row.split(' from ')
    qty = row[0].replace('move ', '')
    direction.append(int(qty))
    row = row[1].split(' to ')
    start = row[0]
    direction.append(int(start))
    end = row[1][0]
    direction.append(int(end))
    print(end)
    directions_clean.append(direction)

# print(directions_clean)

def move_letters(lst):
    qty, start, stop = lst 
    sect_length = len(cargo[start])
    key = sect_length - qty
    removed = cargo[start][key::]
    print("Removed: ", removed)
    cargo[start] = cargo[start][:key]
    cargo[stop] = cargo[stop] + removed[::-1]
    print(cargo[stop])

# def move_letters(lst):
#     qty, start, stop = lst 
#     sect_length = len(test_cargo[start])
#     key = sect_length - qty
#     removed = test_cargo[start][key::]
#     print(lst)
#     print(f"Removed {removed} from {start} to {stop} ")
#     test_cargo[start] = test_cargo[start][:key]
#     test_cargo[stop] = test_cargo[stop] + removed[::-1]
#     print(test_cargo)
    # print(cargo[stop])

# print(cargo)
# move_letters(direction_test)
# print(cargo)
for direction in directions_clean:
    move_letters(direction)
# for test in direction_test:
#     move_letters(test)

# tried CQQBBJFCS

for k, v in cargo.items():
    print(v[-1])
