# your code here ...
import pandas as pd
import requests
class Genius:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_artist(self, search_term):
        search_url = "https://api.genius.com/search"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        params = {
            "q": search_term
        }

        search_response = requests.get(
            search_url,
            headers=headers,
            params=params
        )

        search_data = search_response.json()

        artist_id = (
            search_data["response"]["hits"][0]
            ["result"]["primary_artist"]["id"]
        )

        artist_url = f"https://api.genius.com/artists/{artist_id}"

        artist_response = requests.get(
            artist_url,
            headers=headers
        )

        return artist_response.json()
    
    def get_artists(self, search_terms):
        rows = []

        for search_term in search_terms:
            artist_data = self.get_artist(search_term)

            artist = artist_data["response"]["artist"]

            rows.append({
                "search_term": search_term,
                "artist_name": artist["name"],
                "artist_id": artist["id"],
                "followers_count": artist.get("followers_count")
            })

        return pd.DataFrame(rows)