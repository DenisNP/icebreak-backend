hor_count_odd = 25
hor_count_even = hor_count_odd - 1
ver_count = 12

def initial_state(state):
    colors = []
    for v in range(ver_count):
        hor_count = hor_count_even if v % 2 == 0 else hor_count_odd
        last_color = '#ff0000'
        colors.append([])
        for _ in range(hor_count):        
            colors[v].append(last_color)

    return colors