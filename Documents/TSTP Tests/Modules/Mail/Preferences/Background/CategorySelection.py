import requests
import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
mail_parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(mail_parent_dir)
from Global import Variables


token = str
secret = str
app_id = str 

categories = []

with open(os.path.abspath(os.path.join(mail_parent_dir, 'Global', 'credentials.json')), "r") as f:
    cred = json.loads(f.read())
    token = cred["unsplash"]["access_key"]
    secret = cred["unsplash"]["secret_key"]
    app_id = cred["unsplash"]["application_id"]

# Define function to fetch data
def get_categories():
    try:
        # Make API request
        res = requests.get("{}collections/?client_id={}".format(Variables.unsplash_url,token)).json()

        for cat in res:
            source = cat.get("tags", [{}])[1].get("source", {})  # Get the source dictionary or an empty dictionary if tags or source are not found
            photographer_name = source.get("cover_photo", {}).get("user", {}).get("name", "Unknown")  # Get the photographer's name or "Unknown" if not found

            categories.append({
                "id": cat["id"],
                "description": cat["description"],
                "title": cat["title"],
                "total_photos": cat["total_photos"],
                "source": f"Captured by {photographer_name} on <a href=\"{Variables.unsplash_link}\">Unsplash</a>",
                "cover": source.get("cover_photo", {}).get("urls", {}).get("thumb", "")  # Get the cover photo URL or an empty string if not found
            })
        
        print(categories)
    except requests.RequestException as e:
        print("Request failed:", e)
    except json.JSONDecodeError as e:
        print("JSON decoding failed:", e)
    except KeyError as e:
        print("Key not found in JSON:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
        
get_categories()