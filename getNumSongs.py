import json
import os
from alive_progress import alive_bar

dictOfURIs = {}

dataset_path = r"Dataset\data"

num_files = len([name for name in os.listdir(dataset_path)])

with alive_bar(num_files) as bar:
    for file in os.listdir(dataset_path):
        with open(os.path.join(dataset_path, file), "r") as f:
            data = json.load(f)
            for playlist in data["playlists"]:
                for song in playlist["tracks"]:
                    # if the URI is not in the set then add it with value 1
                    if song["artist_uri"] not in dictOfURIs:
                        # TODO: Fix this
                        dictOfURIs.update({song["artist_uri"]: 1})
                    else:
                        dictOfURIs[song["artist_uri"]] += 1
                    # if it is in the set then increment the value by 1
            bar()

# Only count the songs that appear more than 10 times
newDictOfURIs = {key: value for key, value in dictOfURIs.items() if value > 50}

print(f"Number of songs: {len(newDictOfURIs):,}")