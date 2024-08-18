"""
I've completed this lab, took around 2 hours as I'm new to python and so far I'm understanding why so many people
say this is their favorite language. Your small examples in the lab help a lot especially how python does it's 
lists/truples and the if elif statements. What I did for this project is I made the color_list able to have 
as much inputs as you want. The list is printed and the user inputs what number on the list is the color they choose.
Then that's the color that gets put through the if and elif statements. Correct input checking didn't seem necessary.
The challenges I faced was knowing how to print a list out to the screen then how to convert the userinput into an int.
I went through all the colors and changed around the size of the list and I'm happy and had fun with it.  
"""

color_list = [(227, 66, 52), (205, 96, 144), (28, 134, 238), (250, 250, 70)]

print('Here are the choices of colors:')
for color in color_list:
    print(color_list.index(color), color)

print('Then choose what color you want to examine by choosing a number between 0 and', len(color_list) - 1)
user_input = int(input("Enter the number here: "))
chosen_color = color_list[user_input]

if chosen_color[0] == chosen_color[1]:
    print('The color is a shade of yellow.') 
elif chosen_color[0] == chosen_color[2]:
   print('The color is a shade of magenta.') 
elif chosen_color[1] == chosen_color[2]:
   print('The color is a shade of cyan.') 
elif chosen_color[0] > chosen_color[1] and chosen_color[0] > chosen_color[2]:
    print('The color is reddish.')
elif chosen_color[1] > chosen_color[0] and chosen_color[1] > chosen_color[2]:
    print('The color is greenish.')
else:
    print('The color is blueish.')