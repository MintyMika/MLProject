import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
'''
Each playlist is a JSON file with the following structure:
{
        "name": "musical",
        "collaborative": "false",
        "pid": 5,
        "modified_at": 1493424000,
        "num_albums": 7,
        "num_tracks": 12,
        "num_followers": 1,
        "num_edits": 2,
        "duration_ms": 2657366,
        "num_artists": 6,
        "tracks": [
            {
                "pos": 0,
                "artist_name": "Degiheugi",
                "track_uri": "spotify:track:7vqa3sDmtEaVJ2gcvxtRID",
                "artist_uri": "spotify:artist:3V2paBXEoZIAhfZRJmo2jL",
                "track_name": "Finalement",
                "album_uri": "spotify:album:2KrRMJ9z7Xjoz1Az4O6UML",
                "duration_ms": 166264,
                "album_name": "Dancing Chords and Fireflies"
            },
            {
                "pos": 1,
                "artist_name": "Degiheugi",
                "track_uri": "spotify:track:23EOmJivOZ88WJPUbIPjh6",
                "artist_uri": "spotify:artist:3V2paBXEoZIAhfZRJmo2jL",
                "track_name": "Betty",
                "album_uri": "spotify:album:3lUSlvjUoHNA8IkNTqURqd",
                "duration_ms": 235534,
                "album_name": "Endless Smile"
            },
            {
                "pos": 2,
                "artist_name": "Degiheugi",
                "track_uri": "spotify:track:1vaffTCJxkyqeJY7zF9a55",
                "artist_uri": "spotify:artist:3V2paBXEoZIAhfZRJmo2jL",
                "track_name": "Some Beat in My Head",
                "album_uri": "spotify:album:2KrRMJ9z7Xjoz1Az4O6UML",
                "duration_ms": 268050,
                "album_name": "Dancing Chords and Fireflies"
            },
'''
'''
From the JSON file, we can make tensors of the following:
Track Name, Artist Name, Album Name, Duration

From this we can make a dataset of the following:
Track Name, Artist Name, Album Name, Duration, Playlist Name

We can then use this dataset to train a model to predict the playlist name given the other features

'''

class Song():
    def __init__(self, track_name, artist_name, album_name, duration):
        self.track_name = track_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.duration = duration
    
    def getTensor(self):
        return torch.tensor([self.track_name, self.artist_name, self.album_name, self.duration])

    def __str__(self):
        return "Track Name: " + self.track_name + "\nArtist Name: " + self.artist_name + "\nAlbum Name: " + self.album_name + "\nDuration: " + str(self.duration)


class UniquePlaylist():
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def addSong(self, song):
        self.songs.append(song)
    
    def getTensor(self):
        return torch.tensor([song.getTensor() for song in self.songs])

    def __str__(self):
        return "Playlist Name: " + self.name + "\nSongs: \n" + "\n".join([str(song) for song in self.songs])

