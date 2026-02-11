import numpy as np
np.random.seed(0)
scores = np.random.randint(50, 101, size=(5, 3))
mean_scores = scores.mean(axis=0)
centered_scores = scores - mean_scores
print("Original Scores:\n", scores)
print("\nMean of Each Subject:\n", mean_scores)
print("\nCentered Scores:\n", centered_scores)
