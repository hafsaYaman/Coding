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

