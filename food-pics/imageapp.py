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









# # import os
# from clarifai.rest import ClarifaiApp
# from pprint import pprint   #makes payload look nicer to read

# #need to find out how to use Clarifai API in .env because these arent working
# # CLARIFAI_API_KEY =  os.environ.get('CLARIFAI_API_KEY')
# # app = ClarifaiApp(CLARIFAI_API_KEY)

# app = ClarifaiApp()

# def get_food_tags(image_url):
#     response_data = app.food_tags([image_url])
#     food_tags = {}   #change from array for faster lookup time 
#     for concept in response_data['outputs'][0]['data']['concepts']:
#         # food_tags.append(concept['name'])
#         food_tags[concept['name']] = 1
#         # print('\n'.join(get_food_tags(concept['name'])))
#     return food_tags
# pprint("clarifaiapp.py compiled")


# #line below returns all the relevant tags  (from f(x) above)
# # print('\n'.join(get_food_tags('insertURLhere')))
# # print('\n'.join(get_food_tags(image_url)))
