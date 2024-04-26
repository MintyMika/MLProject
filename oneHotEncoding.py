import numpy as np


# Read the file and extract the artist IDs
with open("Dataset/src/test.txt", "r") as file:
    artists = [int(line.strip()) for line in file]

# Determine the number of unique artists
num_artists = len(set(artists))

# Initialize an empty one-hot encoding matrix
one_hot_matrix = np.zeros((len(artists), num_artists))

# Iterate through each artist and set the corresponding one-hot encoding
for i, artist_id in enumerate(artists):
    one_hot_matrix[i, artist_id - 1] = 1  # Subtract 1 to adjust for 0-based indexing

# Print the one-hot encoding matrix
print(one_hot_matrix)



"""
#Extract categorical columns from the dataframe
#Here we extract the columns with object datatype as they are the categorical columns
categorical_columns = ['Playlist']

#Initialize OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Apply one-hot encoding to the categorical columns
one_hot_encoded = encoder.fit_transform(df[categorical_columns])

#Create a DataFrame with the one-hot encoded columns
#We use get_feature_names_out() to get the column names for the encoded data
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

# Concatenate the one-hot encoded dataframe with the original dataframe
df_encoded = pd.concat([df, one_hot_df], axis=1)

# Drop the original categorical columns
df_encoded = df_encoded.drop(categorical_columns, axis=1)

# Display the resulting dataframe
print(f"Encoded Employee data : \n{df_encoded}")
"""