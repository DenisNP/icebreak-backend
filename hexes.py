import math
import land_mask

hor_count_odd = 101
hor_count_even = hor_count_odd - 1
ver_count = 70

hex_width = 20

normal_color = '#00ff00'
land_color = '#ff0000'

land_hexes = land_mask.mask
build_hexes = []

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
        elif row % 2 == 0 and horizontal == 1:
            c += 1

    # if not is_hex_exists(r, c):
    #     return None
    if not full_hex_exists(r, c):
        return None
    
    return [r, c]

def full_hex_exists(r, c):
    for i in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if not is_hex_exists(r + i, c + k):
                return False
    return True

def is_hex_exists(r, c):
    if r < 1 or c < 1 or r >= ver_count - 1 or c >= hor_count_even - 1:
        return False

    return not is_hex_restricted(r, c)

def is_hex_restricted(r, c):
    for hexs in land_hexes:
        if hexs[0] == r and hexs[1] == c:
            return True
    return False
    
