import os
import json
import numpy as np
import pandas as pd
from alive_progress import alive_bar

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

with alive_bar(num_files) as bar:
    for file in os.listdir(dataset_path):
        # Only go through 25% of the files
        # iters += 1
        # if iters == 101:
        #     break
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
    

# Save only the values of the dictionary to a file
file_name = r"Dataset\src\PlaylistVectors.txt"

with open(file_name, "w") as f:
    with alive_bar(len(dictOfPlaylists)) as bar:
        for key, value in dictOfPlaylists.items():
            # Convert to numpy array
            value = np.array(value)
            # Get only the unique values
            value = np.unique(value)
            # Convert to list
            value = value.tolist()
            f.write(f"{value}\n")
            bar()

# Print the number of playlists
# print(f"Number of playlists: {len(dictOfPlaylists):,}")
