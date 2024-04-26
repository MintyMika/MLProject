import torch
from torch.utils.data import Dataset, DataLoader
from alive_progress import alive_bar

class PlaylistDataset(Dataset):
    def __init__(self, file_path):
        self.file_path = file_path
        self.playlists = self._load_playlists()

    def _load_playlists(self):
        with open(self.file_path, 'r') as file:
            playlists = [eval(line.strip()) for line in file.readlines()] # Read and parse each line as a list
        return playlists

    def __len__(self):
        return len(self.playlists)

    def __getitem__(self, idx):
        return torch.tensor(self.playlists[idx])

def collate_fn(batch):
    # Pad playlists in batch to make them equal length
    max_len = max(len(playlist) for playlist in batch)
    padded_batch = [torch.nn.functional.pad(playlist, (0, max_len - len(playlist))) for playlist in batch]
    return torch.stack(padded_batch)

from alive_progress import alive_bar

def main():
    file_path =  r"Dataset/src/MinimizedPlaylistVectors.txt"

    dataset = PlaylistDataset(file_path)

    number_of_playlists = len(dataset)
    batch_size = 1000

    # Use collate_fn to handle padding of variable-length playlists
    data_loader = DataLoader(dataset, batch_size=batch_size, collate_fn=collate_fn)
    with alive_bar(int(number_of_playlists / 1000)) as bar:
        for batch in data_loader:
            # print(batch.shape)  # Shape will be (batch_size, max_length_of_playlist)
            pass
        bar()

if __name__ == "__main__":
    main()

