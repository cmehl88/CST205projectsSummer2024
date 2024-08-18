"""
This lab is completed, and was a great introduction to functions and dictionaries. I didn't
know you could have a dictionary in a dictionary so was cool seeing how to extract the 
information from it. Some challeneges I faced was the formatting to get to those embedded 
dictionaries along with how to convert RGB into hex and vise versa and the more I use python
the more I'm liking it from other languages. I was having trouble as well with returns in
functions so I turned them into print statements instead and seem to work well as these 
functions are only called once each and in order. Using the terminal too I'm finding pretty
fun as well as I haven't coded like this in a while and I thought errors would be much 
harder to fix but the terminal is actually pretty good at saying what the problems are or where at.
"""
import random
color_dictionary = {
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'magenta': (255, 0, 255)
}

# Using random from the slide example, picks a random color from the dictionary
random_color = random.choice(list(color_dictionary.keys()))
# Get the key values of the randomly chosen color
rgb_values = color_dictionary[random_color]
# Pick a random channel with the options being (R, G, or B)
channel_name = random.choice(['red', 'green', 'blue'])
# Using another dictionary, using channel_name's color gets that value chosen
channel_value = rgb_values[{'red': 0, 'green': 1, 'blue': 2}[channel_name]]
# Print the sentence describing the random color, random channel, and the value
print(f"The {channel_name} channel of {random_color} has value {channel_value}.")

tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

# Let clay_creek_color get to the color tuple in result, in color, and 0 being red channel
clay_creek = tineye_sample["result"][0]["color"]
# Get the red channel's value 
red_channel_value = clay_creek[0]
# print red_channel_value
print("The red channel value of Clay Creek:", red_channel_value)

# Do the same thing for the blue channel for Seal Brown
seal_brown = tineye_sample["result"][1]["color"]
blue_channel_value = clay_creek[1]
print("The blue channel value of Seal Brown:", blue_channel_value)

def rgb_values():
    red = int(input("Enter red: "))
    green = int(input("Enter green: "))
    blue = int(input("Enter blue: "))
    print(f"thank you, your RGB color is ({red}, {green}, {blue})")
rgb_values()

def rgb_argument(the_tuple):
    red, green, blue = the_tuple
    print("The red channel intensity is:", red)
    print("The green channel intensity is:", green)
    print("The blue channel intensity is:", blue)

# the_tuple is what is seems, then it gets passed to the function
the_tuple = (23, 240, 99)
rgb_argument(the_tuple)

def rgb_to_hexadecimal(tuple_2):
    # make sure the range is between 0 and 255
    r, g, b = tuple_2
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    # Had to look up how to convert from a byte to hex and it looks like python makes it very simple with one line of code 
    hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)
    print(f"This is the hex value: {hex_value}") 
    
tuple_2 = (40, 255, 50)
rgb_to_hexadecimal(tuple_2)

def hex_to_rgb(the_hex_value):
    # This is how to convert the first two characters to an integer in hex base 16 which is the 16 at the end
    r = int(the_hex_value[0:2], 16)  
    g = int(the_hex_value[2:4], 16)  
    b = int(the_hex_value[4:6], 16)  
    print(f"The RGB is ({r}, {g}, {b})") 

the_hex_value = "28ff32"
hex_to_rgb(the_hex_value)
