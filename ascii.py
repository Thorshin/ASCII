from PIL import Image

im = Image.open("beach.jpg")
width, height = im.size
matrix = [[None] * width for _ in range(height)]
im= im.convert("RGB")
for y in range(height):
    for x in range(width):
        R, G, B = im.getpixel((x, y))
        matrix[y][x] = int((R + G + B) / 3)

str_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/fjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for y in range(height):
    for x in range(width):
        matrix[y][x] = str_chars[int(matrix[y][x] / 4)]

matrix_str = '\n'.join([' '.join(map(str, row)) for row in matrix])

print(matrix_str)           



