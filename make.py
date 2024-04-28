from PIL import Image, ImageDraw

def text_to_rgb(text):
    return [(ord(char) >> 6, (ord(char) >> 3) & 7, ord(char) & 7) for char in text]

def create_color_barcode(text, width=10, height=50):
    rgb_values = text_to_rgb(text)
    num_strips = len(rgb_values)
    image = Image.new("RGB", (num_strips * width, height), "white")
    draw = ImageDraw.Draw(image)

    for i, (r, g, b) in enumerate(rgb_values):
        color = (r * 32, g * 32, b * 32) 
        draw.rectangle([i * width, 0, (i + 1) * width, height], fill=color)

    return image