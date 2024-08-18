"""
Carson Mehl
Cst205
7/14/2024
Lab - Web Scrapping
Summary: Using beautiful Soup, lxml, and wordcloud, use beautiful soup to
grab the image URL, scrap paragraph text from the logitech website and display it 
as a word cloud.
Website link: https://www.logitech.com/en-us
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
from wordcloud import WordCloud
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

# Put the website as a variable/object
my_site='https://www.logitech.com/en-us'

# Open the site
site_html=urlopen(my_site)

soup = BeautifulSoup(site_html.read(), 'lxml')

# find all images
# can replace 'img' with other html tags
images = soup.findAll('img')

# loop through list of images and retrieve 'src' attribute
for image in images:
    print(image['src'])

# Task 2
# IMAGE URL: https://resource.logitech.com/w_316,c_limit,f_auto,q_auto,dpr_1.0/d_transparent.gif/content/dam/logitech/en/navigation/shop-mice.png?v=1

# Task 3
# Name an object, then find all text in paragraph, the same as you do with soup above
paragraphs = soup.find_all('p')

# Go over each paragraph and sort by joinging the strings together using .join
text = " ".join(paragraph.get_text() for paragraph in paragraphs)

# Generate the word cloud with those dimentions, and background color
wordcloud = WordCloud(width=1000, height=600, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Extra Notes --------------------------
# This line will print out all the text on the webpage of that website
# print(soup.get_text())

# This will print the title of the website, what is shown on the tab of the browser
# print(soup.title.text)

# print out a portion of the HTML
# print(site_html.read()[5000:5400])

# Image Notes ---------------------------
# find all images
# can replace 'img' with other html tags
#images = soup.findAll('img')

# loop through list of images and retrieve 'src' attribute
#for image in images:
#    print(image['src'])
