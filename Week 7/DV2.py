"""
Carson Mehl
Cst205
7/25/2024
Lab - Data Visualization
Summary: Gets text from DV.py and displays the most common 
words from the text onto a bar chart based on the highest
top five word count.
Dependencies: Using the "the_text" and "stop-words" string and list from DV.py file.
"""

import string
import matplotlib.pyplot as plt
from DV import the_text, stop_words
from collections import Counter

# Task 3
# Split the text into words, remove the punctuation  
# Turn the words into lower case and ready for counting
words = [word.strip(string.punctuation).lower() for word in the_text.split()]

# Create a new list of the text excluding any word that is in the stop_words list
new_list = [word for word in words if word not in stop_words]

# Count each word in the new_list and store into word_counts
word_counts = {}
for word in new_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Convert the word counts to a Counter object to use the most_common() method 
# This is by importing Counter from collections
word_counts_counter = Counter(word_counts)

# Get the top 5 most common words using the most_common method from that collections import
top_5_words = word_counts_counter.most_common(5)

# Using the dict method to create a dictionary from the top 5 words with their counts nicely
top_five = dict(top_5_words)

# Task 4
# Plotting the bar chart with count on the y axis and the word on the x axis, example from slides 
plt.bar(top_five.keys(), top_five.values())
plt.title("Top 5 Most Common Words from the text")
plt.ylabel("Count")
plt.xlabel("Word")
plt.show()