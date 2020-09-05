# Import plotting modules and np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Set default Seaborn style

sns.set()

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length, bins = n_bins)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
