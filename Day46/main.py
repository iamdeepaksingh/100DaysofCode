# Author: Deepak Kumar Singh
# Description: Spotify playlist using BeautifulSoup.
# Date Created: 22/02/2022
# Date Modified: 22/02/2022

import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_UNIQUE_CLIENT_ID = 'put your client id'

CLIENT_SECRET = 'put your secret code'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_UNIQUE_CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

user_input = input("Which year do you want to travel to ? Type date in format yyyy-mm-dd.")

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all(name='h3', class_="a-no-trucate")

artist_name = soup.select(".c-label.a-font-primary-s")
artist_list = [artist.getText().strip() for artist in artist_name]

song_titles = [song.getText().strip() for song in songs]
print(artist_list)

if song_titles is not None:
    for song in range(len(song_titles)):
        with open("Songs.txt", "a") as file:
            file.writelines(f" {user_input} : {song+1}: {song_titles[song]} \n")
            # print(f" {song+1}: {song_titles[song]}")

song_uris = []
year = user_input.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)


#sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)