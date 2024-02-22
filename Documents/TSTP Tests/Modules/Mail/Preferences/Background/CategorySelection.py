import requests
import sys
import os
import json
import asyncio

current_dir = os.path.dirname(os.path.abspath(__file__))
mail_parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(mail_parent_dir)
from Global import Variables

categories = []

# Define asynchronous function to fetch data
async def get_categories():
    try:
        # Make API request
        data =  Variables.unsplash_get(Variables.get_collections)
        
        for cat in data:
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

# Run the asynchronous function
asyncio.run(get_categories())
