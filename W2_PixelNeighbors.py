import numpy as np

image = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

x, y = 1, 1
rows, cols = image.shape

komsu_4 = []
if x > 0: komsu_4.append(image[x-1, y])
if y > 0: komsu_4.append(image[x, y-1])
if y < cols - 1: komsu_4.append(image[x, y+1])
if x < rows - 1: komsu_4.append(image[x+1, y])

komsu_8 = []
for i in range(x-1, x+2):
    for j in range(y-1, y+2):
        if (0 <= i < rows and 0 <= j < cols) and (i, j) != (x, y):
            komsu_8.append(image[i, j])

komsu_d = []
if x > 0 and y > 0: komsu_d.append(image[x-1, y-1])
if x > 0 and y < cols - 1: komsu_d.append(image[x-1, y+1])
if x < rows - 1 and y > 0: komsu_d.append(image[x+1, y-1])
if x < rows - 1 and y < cols - 1: komsu_d.append(image[x+1, y+1])

komsu_m = sorted(komsu_4 + komsu_d)

print("4 komşulari:", komsu_4)
print("8 komşulari:", komsu_8)
print("d komşulari:", komsu_d)
print("m komşulari:", komsu_m)
