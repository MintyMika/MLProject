import pandas as pd
import random
import ast
from sklearn.preprocessing import OneHotEncoder

# Function to generate random pairs of artistNum from a list
def generate_random_pairs(artistNum):
    pairs = set()  # Using a set to avoid duplicate pairs
    while len(pairs) < 3:  # Generate 3 unique pairs
        pair = tuple(random.sample(artistNum, 2))  # Randomly select two artistNum
        pairs.add(pair)  # Add the pair to the set
    return list(pairs)  # Convert set to list for consistent order


# Open the file
with open('test.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Convert the string representation of list to a Python list
        artistNum = ast.literal_eval(line.strip())

        # Generate random pairs of artistNum
        random_pairs = generate_random_pairs(artistNum)

        # Print or store the random pairs
        print(random_pairs)

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