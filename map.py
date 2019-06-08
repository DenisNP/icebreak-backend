import numpy as np

def generate_eco_region(zeros_num,total_dots):
    arr = np.array([0] * zeros_num + [1] * (total_dots - zeros_num))
    np.random.shuffle(arr)
    return arr.reshape(3, 3)

def generate_line_of_regions(regions_in_line,zeros_num, total_dots):
    line_arr = generate_eco_region(zeros_num, total_dots)
    for x in range(regions_in_line):
        line_arr = np.hstack((line_arr, generate_eco_region(zeros_num, total_dots)))
    return line_arr
        
def generate_rectangle_of_regions(hregions, vregions, zero_num, total_dots):
    result_arr = generate_line_of_regions(hregions,zero_num,total_dots)
    for y in range(vregions):
        result_arr = np.vstack((result_arr, generate_line_of_regions(hregions, zero_num, total_dots)))
    return result_arr

result = generate_rectangle_of_regions(7,3,8,9)    
print(result)
print ('------------------------------------')

print (np.array(np.where(result == 1)).T)