import colorgram
rgb_colours = []
colours = colorgram.extract("image.jpg", 30)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

print(rgb_colours)
