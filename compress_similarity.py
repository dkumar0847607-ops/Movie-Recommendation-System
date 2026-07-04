import pickle
import numpy as np

# Load similarity matrix
similarity = pickle.load(open("models/similarity.pkl", "rb"))

print("Original dtype:", similarity.dtype)
print("Original size:", similarity.nbytes / (1024**2), "MB")

# Convert to float32
similarity = similarity.astype(np.float32)

print("New dtype:", similarity.dtype)
print("New size:", similarity.nbytes / (1024**2), "MB")

# Save again
pickle.dump(similarity, open("models/similarity.pkl", "wb"))

print("Done!")