import os
from clarifai.rest import ClarifaiApp
from pprint import pprint   #makes payload look nicer to read

#need to find out how to use Clarifai API in .env because these arent working
# CLARIFAI_API_KEY =  os.environ.get('CLARIFAI_API_KEY')
# app = ClarifaiApp(CLARIFAI_API_KEY)

app = ClarifaiApp()

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])
    tag_urls = {}   #change from array for faster lookup time 
    for concept in response_data['outputs'][0]['data']['concepts']:
        # tag_urls.append(concept['name'])
        tag_urls[concept['name']] = 1
    return tag_urls

pprint("clarifaiapp.py compiled")


#line below returns all the relevant tags  (from f(x) above)
# print('\n'.join(get_relevant_tags('insertURLhere')))
