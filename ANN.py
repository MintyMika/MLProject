import ast
import random
import torch
import torch.nn as nn
import torch.optim as optim
import time
from alive_progress import alive_bar

# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Read the text file and parse each line to get the list of artists
artists_data = []
with open('Dataset\src\PlaylistVectors.txt', 'r') as file:
    print("Reading file...")
    num_lines = 10000  # Number of lines in the file
    with alive_bar(num_lines) as bar:
        for line in file:
            artists = ast.literal_eval(line.strip())
            artists_data.append(artists)
            bar()

# Function to generate random pairs of artists from a list
def generate_random_artist_pairs(artists):
    pairs = set()  # Using a set to avoid duplicate pairs
    while len(pairs) < 3:  # Generate 3 unique pairs
        pair = tuple(random.sample(artists, 2))  # Randomly select two artists
        pairs.add(pair)  # Add the pair to the set
    return list(pairs)  # Convert set to list for consistent order

# Generate training data
training_data = []
print("Generating training data...")
with alive_bar(len(artists_data)) as bar:
    for artists in artists_data:
        random_pairs = generate_random_artist_pairs(artists)
        for pair in random_pairs:
            training_data.append(pair)
        bar()

# Shuffle training data
random.shuffle(training_data)

# Convert artists to unique IDs
artist_to_id = {artist: i for i, artist in enumerate(set(artist for pair in training_data for artist in pair))}
num_artists = len(artist_to_id)

# Convert pairs of artists to pairs of their corresponding IDs
training_data_ids = [(artist_to_id[artist1], artist_to_id[artist2]) for artist1, artist2 in training_data]

# Split data into input and target
print("Splitting data...")
X = torch.tensor([data[0] for data in training_data_ids], dtype=torch.float).view(-1, 1).to(device)  # Reshape for single feature
y = torch.tensor([data[1] for data in training_data_ids], dtype=torch.long).to(device)

# Define the model architecture
input_size = 1  # Number of input neurons
hidden_size = 64  # Number of neurons in the hidden layer
output_size = num_artists  # Number of output neurons

class ArtistPredictor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ArtistPredictor, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the model and move it to the GPU if available
model = ArtistPredictor(input_size, hidden_size, output_size).to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Measure the time taken for training
start_time = time.time()

# Train the model
num_epochs = 10
print("Training model...")
with alive_bar(num_epochs) as bar:
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        bar()

# Calculate the elapsed time
elapsed_time = time.time() - start_time
print(f"Training completed in {elapsed_time:.2f} seconds.")

# Evaluate the model (optional)
with torch.no_grad():
    outputs = model(X)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y).sum().item() / y.size(0)
    print('Accuracy:', accuracy)
