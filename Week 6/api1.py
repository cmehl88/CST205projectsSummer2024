"""
Carson Mehl
Cst205
7/14/2024
Lab - API Task 1 and 2
Summary: This api returns a cat image url or an error if something is wrong.
"""

import json
import requests

# Task 1 -------------------
# Name of API: TheCatAPI
# This is an API that offers the user cat related data like images videos and information like fun facts.
# Some information requries a key to use from this api but for abtaining an image you don't need one.

# Task 2 -------------------
# The endpoint URL, (this example was inspired from the websites available examples)
endpoint = 'https://api.thecatapi.com/v1/images/search'

# Use a try except for the image
try:
    # Make a GET request to the API
    response = requests.get(endpoint)
    
    # Check to make sure the HTTP request was successful
    response.raise_for_status()
    
    # Read the json file response
    data = response.json()
    
    # Extract the cat image URL
    cat_image_url = data[0]['url']
    
    # Print the cat image URL
    print(f'Cool Random Cat Image URL: {cat_image_url}')

    # If there is a problem print here
except requests.exceptions.RequestException as e:
    print(f'Something went wrong --> {e}')

