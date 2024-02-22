import requests
import json
import asyncio


token = str
secret = str
app_id = str 

with open('Global/credentials.json', "r") as f:
    cred = json.loads(f.read())
    token = cred["unsplash"]["access_key"]
    secret = cred["unsplash"]["secret_key"]
    app_id = cred["unsplash"]["application_id"]


preferences = {"background_URL" : "", "theme" : "", }
unsplash_link = "https://unsplash.com/"


url = "https://api.unsplash.com/"

get_collections= "{}collections/".format(url)
#! Url / Collection ID
get_collection_photos = "{}colections/{}/photos"
#! URl / Photo ID
get_photo = "{}photos/{}"


post_personal_collection = "{}collections".format(url)
#! URL / Personal Collection ID
post_photo_Personal = "{}collections/{}/add"


#! URL / Personal Collection ID
delete_photo_Personal = "{}collections/{}/remove"



def unsplash_get(endpoint):
    response = requests.get(f"{endpoint}{token}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status() 
    


