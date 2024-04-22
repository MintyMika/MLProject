import os
import json
import pandas as pd
from alive_progress import alive_bar
import threading

dictOfArtists = json.load(open(r"Dataset\src\dictOfURIs.json", "r"))

# Make a new dictionary with artist_URI as key and a number as value
numberedArtists = {}
for index, artist in enumerate(dictOfArtists):
    numberedArtists.update({artist: index})

# Make a new dictionary with playlist as the key and list of artists numbers as the value
dictOfPlaylists = {}

dataset_path = r"Dataset\data"

num_files = len([name for name in os.listdir(dataset_path)])

iters = 0

with alive_bar(int(num_files/4)) as bar:
    for file in os.listdir(dataset_path):
        # Only go through 25% of the files
        iters += 1
        if iters == 250:
            break
        with open(os.path.join(dataset_path, file), "r") as f:
            data = json.load(f)
            for playlist in data["playlists"]:
                list_of_artists = []
                for song in playlist["tracks"]:
                    if song["artist_uri"] in dictOfArtists:
                        if playlist["pid"] not in dictOfPlaylists:
                            dictOfPlaylists.update({playlist["pid"]: [numberedArtists[song["artist_uri"]] for song in playlist["tracks"] if song["artist_uri"] in dictOfArtists]})
                        else:
                            dictOfPlaylists[playlist["pid"]].extend([numberedArtists[song["artist_uri"]] for song in playlist["tracks"] if song["artist_uri"] in dictOfArtists])
        bar()
    

# Save the dictionary to a file
with open(r"Dataset\src\dictOfPlaylists.json", "w") as f:
    json.dump(dictOfPlaylists, f)

# Print the number of playlists
print(f"Number of playlists: {len(dictOfPlaylists):,}")
