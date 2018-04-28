#import dependencies
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

#instantiate your pipeline component objects
scaler = StandardScaler()
kmeans = KMeans(n_clusters=2)
pipeline = make_pipeline(scaler, kmeans)

#plotting different n_clusters and plotting the inertias and using the elbow rule to select optimal k
ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()


#

#fit your pipeline to your data
pipeline.fit(X)

#generate labels based on your model predictions
labels = pipeline.predict(X)

#create a dataframe for your labeled predictions vs that of your true class labels
df = pd.DataFrame({'predictedlabels': labels, 'truelabels': y})

#create a cross tab to see how your cluster labels correspond to your true class labels
ct = pd.crosstab(df['labels'], df['truelabels'])
print(ct)

#you can also create a sorted list to see the trends in your predicted vs true class labels, which ones are growing the in a certain direction
print(df.sort_values('labels'))
