def get_free(tables, timeslot):
    free = []
    for index in range(1, len(tables[0])):
        if tables[timeslot][index] =='o':
            free.append(tables[0][index])
    return free

restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1, 'o', 'x', 'o', 'o', 'o', 'o'],
    [2, 'o', 'o', 'o', 'o', 'x', 'o'],
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],
    [4, 'o', 'o', 'x', 'o', 'o', 'x'],
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],
    [6, 'x', 'o', 'o', 'o', 'o', 'o']
]

def find_table_party(tables, timeslot, party_size):
    for table in range(1, len(tables[0])):
        capacity = int(tables[0][table].split('(')[1].split(')')[0])
        if table[timeslot][table]=='o' and capacity >=party_size:
            return tables[0][table]
    return None


def all_for_party(tables, timeslot, party_size):
    suitable = []
    for index in range(1, len(tables[0])):
        capacity = int(tables[0][index].split('(')[1].split(')')[0])
        if restaurant_tables[timeslot][index] == 'o' and capacity >= party_size:
            suitable.append(tables[0][index])
    return suitable


def combined_party_tables(tables, timeslot, party_size):
    combinations = []
    for index in range(1, len(tables[0])-1):
        capacity = int(tables[0][index].split('(')[1].split(')')[0])
        next_capacity = int(tables[0][index + 1].split('(')[1].split(')')[0])
        if tables[timeslot][index] == 'o' and capacity >= party_size:
            combinations.append([tables[0][index]])
        if tables[timeslot][index] == 'o' and restaurant_tables[timeslot][index + 1] == 'o' and (capacity + next_capacity) >= party_size:
            combinations.append([tables[0][index], tables[0][index + 1]])
    return combinations




size = 4
print(combined_party_tables(restaurant_tables, 1, size))