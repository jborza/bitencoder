from PIL import Image, ImageFont, ImageDraw, ImageEnhance

width = 320
height = 160

block_size = (32,32)

row_capacity = width / block_size[0]
column_capacity = height / block_size[1]

#640 / 32 = 20
#480 / 32 = 15
#total 300 bytes

#320 / 32 = 10; 160 / 32 = 5; 50 bytes

#input_data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

#8 colors representing 3 bits

color8 =['black', 'white','red','blue','yellow','green',' magenta','cyan']
bit_to_color = {'000':'black', 
'001':'blue', 
'010':'lime',
'011':'cyan',
'100':'red',
'101':'magenta',
'110':'yellow', 
'111':'white'}

def char_to_bits(ch):
    #bin() returns 0b000000 - remove the 0b prefix
    #return bin(ch)[2:]
    return format(ch, "08b")

def bitstream(string):
    bits = [char_to_bits(ch) for ch in string]
    return ''.join(bits)

def bitgroups(string,length):
    return [string[start:start+length] for start in range(0, len(string), length)]

input_data = b'Hello, World! Boo!'
input_bits = bitstream(input_data)
#todo pad the bits to multiples of 3 bit

pixel_index = 0

# create image with size (w,h) and white background
img = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(img)

#take group of 3 bits and assign a color
groups = bitgroups(input_bits, 3)
for group in groups:
    color = bit_to_color[group]

    row = pixel_index % row_capacity
    column = int(pixel_index / row_capacity)
    print('%s -> %s @ %d,%d' % (group, color , row, column))
    pixel_index = pixel_index + 1
    draw.rectangle([row * 32, column * 32, (row+1)*32,(column+1)*32],fill=color)

# put text on image
#button_draw = ImageDraw.Draw(img)
#button_draw.text((20, 20), "very loooooooooooooooooong text", font=ImageFont.truetype("arial"), fill='black')

# save in new file
img.save("output.png", "PNG")