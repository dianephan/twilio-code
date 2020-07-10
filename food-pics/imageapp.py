from clarifai.rest import ClarifaiApp
from pprint import pprint   #makes payload look nicer to read
app = ClarifaiApp()

def get_food_tags(image_url):
    response_data = app.tag_urls([image_url])
    food_tags = {}   #dictionary data structure for faster lookup time 
    for concept in response_data['outputs'][0]['data']['concepts']:
        food_tags[concept['name']] = 1
    return food_tags
pprint("imageapp.py compiled")