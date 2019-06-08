import math

hor_count_odd = 101
hor_count_even = hor_count_odd - 1
ver_count = 70

hex_width = 20

land_hexes = [
              list(map(lambda x: [0, x], range(58))) + \
              list(map(lambda x: [1, x], range(58))) + \
              list(map(lambda x: [2, x], range(57))) + \
              list(map(lambda x: [3, x], range(57))) + \
              list(map(lambda x: [4, x], range(56))) + \
              list(map(lambda x: [5, x], range(56))) + \
              list(map(lambda x: [6, x], range(54))) + \
              list(map(lambda x: [7, x], range(54))) + \
              list(map(lambda x: [8, x], range(53))) + \
              list(map(lambda x: [9, x], range(53))) + [[9,86]] + [[9,87]] + list(map(lambda x: [9, x], range(92, 99))) + \
              list(map(lambda x: [10, x], range(51))) + list(map(lambda x: [10, x], range(85, 89))) + list(map(lambda x: [10, x], range(91, 99))) + \
              list(map(lambda x: [11, x], range(51))) + list(map(lambda x: [11, x], range(86, 89))) + list(map(lambda x: [11, x], range(91, 99))) + \
              list(map(lambda x: [12, x], range(51))) + [[12, 87]] + [[12, 88]] + list(map(lambda x: [12, x], range(90, 99))) + 
              list(map(lambda x: [13, x], range(51))) + list(map(lambda x: [13, x], range(90, 99))) + \
              list(map(lambda x: [14, x], range(50))) + list(map(lambda x: [14, x], range(90, 99))) + \
              list(map(lambda x: [15, x], range(50))) + list(map(lambda x: [15, x], range(91, 99))) + \
              list(map(lambda x: [16, x], range(49))) + list(map(lambda x: [16, x], range(91, 99))) + \

              list(map(lambda x: [17, x], range(51))) + list(map(lambda x: [17, x], range(90, 99))) + \
              list(map(lambda x: [18, x], range(52))) + list(map(lambda x: [18, x], range(90, 99))) + \
              list(map(lambda x: [19, x], range(53))) + list(map(lambda x: [19, x], range(91, 99))) + \
              list(map(lambda x: [20, x], range(44))) + list(map(lambda x: [20, x], range(91, 99))) + \
              list(map(lambda x: [21, x], range(56))) + list(map(lambda x: [21, x], range(91, 99))) + \
              list(map(lambda x: [22, x], range(57))) + list(map(lambda x: [18, x], range(90, 99))) + \
              list(map(lambda x: [23, x], range(58))) + list(map(lambda x: [19, x], range(91, 99))) + \
              list(map(lambda x: [24, x], range(57))) + list(map(lambda x: [20, x], range(91, 99))) + \
              list(map(lambda x: [25, x], range(57))) + list(map(lambda x: [21, x], range(91, 99)))
             ]               

def initial_state(state):
    colors = []
    for v in range(ver_count):
        hor_count = hor_count_even if v % 2 == 0 else hor_count_odd
        last_color = '#0000ff'
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

def neighbour_hex(row, col, horizontal, vertical):
    r = row
    c = col

    if vertical == 0:
        c += horizontal
    else:
        r -= vertical
        if row % 2 == 1 and horizontal == -1:
            c -= 1
        elif row % 2 == 1 and horizontal == 1:
            c += 1

    # exclude edges
    if r < 1 or c < 1 or r >= ver_count or c >= hor_count_even:
        return None
    
    return [r, c]

def is_hex_exists(r, c):
    if r < 1 or c < 1 or r >= ver_count or c >= hor_count_even:
        return None

    return True
    
    