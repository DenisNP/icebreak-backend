import math

hor_count_odd = 25
hor_count_even = hor_count_odd - 1
ver_count = 12

hex_width = 80

def initial_state(state):
    colors = []
    for v in range(ver_count):
        hor_count = hor_count_even if v % 2 == 0 else hor_count_odd
        last_color = '#ff0000'
        colors.append([])
        for _ in range(hor_count):        
            colors[v].append(last_color)

    return colors


def get_coords(row, column):
    if row % 2 == 0:
        x = int(hex_width / 2 + hex_width * column)
    else:
        x = int(hex_width * (column - 1))
    y = int(hex_width / math.sqrt(3)/2 + 3/(2 * math.sqrt(3)) * hex_width * row) 

    return [x, y]
