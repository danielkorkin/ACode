import numpy as np

def rgb_to_text(rgb_values):
    chars = [chr((r >> 5) * 64 + ((g >> 5) * 8) + (b >> 5)) for r, g, b in rgb_values]
    return ''.join(chars)

def read_color_barcode(image, width=10):
    pixels = np.array(image)
    height = image.height
    num_strips = image.width // width
    rgb_values = []

    for i in range(num_strips):
        strip = pixels[:, i*width:(i+1)*width]
        avg_color = tuple(np.mean(strip.reshape(-1, 3), axis=0).astype(int))
        rgb_values.append(avg_color)

    return rgb_to_text(rgb_values)