# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

#normalize the data first before merging. clustering works best to have normalized the variances
normalized_samples = normalize(samples)

# Calculate the linkage: mergings
mergings = linkage(normalized_samples, method='complete')

#true clas labels
labels = df[target].values

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=labels,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()
