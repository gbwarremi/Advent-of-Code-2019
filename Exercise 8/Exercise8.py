
# Image dimensions
pixels_width = 25
pixels_height = 6
layer_size = pixels_width * pixels_height

# Read the data file
data = []
with open('input_Day8.txt') as f:
    while True:
        line = f.read(layer_size)
        if not line:
            print('End of file')
            break
        data.append(line)


# Part 1: Find layer with least zeros and then return the result of the number of 1's * number of 2's on this layer.

zeros = []    # List to store the zeros counts

for i in data:
    zeros.append(i.count('0'))    # Count zeros and store in list.

least_zeros_layer = zeros.index(min(zeros))

ones = int(str(data[least_zeros_layer]).count('1'))    # Count ones in layer with least zeros
twos = int(str(data[least_zeros_layer]).count('2'))    # Count twos in layer with least zeros
print(f'Part 1 (File Validation): Number of ones * number of twos: {ones * twos}')

# Part 2: Decode Image
decoded_image = ['?' for i in range(layer_size)]    # Set up template for decoded image

# Cycle through all layers and apply the first non-transparent value into the decoded image
for layer in data:
    for i in range(layer_size):
        if decoded_image[i] == '?':
            if int(layer[i]) == 1:
                decoded_image[i] = 'O'
            elif int(layer[i]) == 0:
                decoded_image[i] = ' '

# Print the decoded image based on the image width and height
for i in range(1, layer_size+1):
    print(decoded_image[i-1], end = '')
    if i % pixels_width == 0:
        print('')



