from noise import pnoise2

arr = 10 * list(10 * [0])
print(arr)
for i in range(10):
    for k in range(10):
        arr[i][k] = pnoise2(i/10, k/10)

print(arr)
