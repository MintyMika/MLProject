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
                list_of_artists = []
                for song in playlist["tracks"]:
                    # if the URI is not in the set then add it with value 1
                    if song["artist_uri"] not in dictOfURIs and song["artist_uri"] not in list_of_artists:
                        dictOfURIs.update({song["artist_uri"]: [1, song["artist_name"]]})
                        list_of_artists.append(song["artist_uri"])
                        
                    if song["artist_uri"] in list_of_artists:
                        continue

                    else:
                        dictOfURIs[song["artist_uri"]][0] += 1
                        list_of_artists.append(song["artist_uri"])
            bar()


# open a file to write the dictionary to
file_name = r"src\dictOfURIs.json"

# Only count the songs that appear more than 50 times
newDictOfURIs = {}
dictofArtists = {}
for key, value in dictOfURIs.items():
    if value[0] > 50:
        newDictOfURIs.update({key: value})
        dictofArtists.update({key: value[1]})

with open(file_name, "w") as f:
    json.dump(dictofArtists, f)

print(f"Number of Artists: {len(newDictOfURIs):,}")