import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
import numpy as np
import matplotlib.pyplot as plt
import os
import json
from time import sleep
from alive_progress import alive_bar
import getDataset as gd


def main():
    
    numOfSongs = 2262292 # 2,262,292 is the number of unique songs in the dataset

    # Load and prepare the dataset
    
    playlists = gd.getPlaylists() # This returns a list of UniquePlaylist objects there should be 1 million of them
    # print the number of playlists in 1,000,000 format
    print(f"Number of playlists: {len(playlists):,}")


    # Creating the ML




    return


if __name__ == "__main__":
    main()