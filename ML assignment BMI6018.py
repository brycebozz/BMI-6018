import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import silhouette_score

cols = ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'] #Manually made column names.
# Im using the Breast Cancer Data Set.

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data', names=cols)
print(list(df.columns))
df = df.dropna() #getting rid of rows with no values
print(df.sample(5)) #testing to see if it worked
print(df.head())
new_df = pd.get_dummies(df)  #since there a qualitative values I need to convert all values to quantifiable values. .getdummies() does that
print(list(new_df.columns))
scaler = StandardScaler()
scaled_df = scaler.fit_transform(new_df)
pca = PCA() #I have to use PCA to keep the dimensions to two since I have mare than two variables. Otherwise I get an error.
#I found two way to bring it to two dimensions PCA and MDS. I tried MDS first but got inconsistent results so I switch to PCA.
pca.fit(scaled_df)
plt.figure(figsize = (10,8))
#Found online, to figure out the number of components to use you need to find the amount that has a cumulative explained variance closest to 80%. That number was 21.
plt.plot(range(1,44), pca.explained_variance_ratio_.cumsum(), marker='o', linestyle='--')
plt.title('Explained Variance by Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.show()
pca = PCA(n_components = 21)
pca.fit(scaled_df)
pca.transform(scaled_df)
scores_pca = pca.transform(scaled_df)
#Below is to do the Elbow Method.
ssd = []
for i in range(1, 20):
    kmeans_pca = KMeans(n_clusters = i, random_state = 42).fit(scores_pca)
    ssd.append(kmeans_pca.inertia_)
plt.figure(figsize = (10,8))
plt.plot(range(1,20),ssd, marker = 'o', linestyle = '--')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('SSD')
plt.show() #Elbow method i want to find the number where the line just stops to steeply decline. It looks like 2 but  it could be 3 as well. I want to confirm with follow up.
#Since the Elbow Method didn't give me a strong line to really tell i also looked at silhouette score. The score closest to one is the closest to 1 is the strongest.
for x in range(2,50):
    n_clusters = x
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(scaled_df)# Calculate silhouette score
    silhouette_avg = silhouette_score(scaled_df, labels)
    print("Silhouette Score:", x, silhouette_avg)
    #strongest silhouette score is 2 with a score of 0.15. Which isnt great but its the best I have.
kmeans_pca = KMeans(n_clusters = 2, random_state = 42).fit(scores_pca)
df_pca = pd.concat([new_df.reset_index(drop = True), pd.DataFrame(scores_pca)], axis = 1)
comp = []
for x in range(1,22):
    comp.append('Component ' + str(x))

df_pca.columns.values[-21:] = comp
centroids = kmeans_pca.cluster_centers_#This created centroids
df_pca['Cluster'] = kmeans_pca.labels_
#Chose components 1 and 2 to keep things simple I could use other components for other graphs but just stuck with one graph.
x_axis = df_pca['Component 1']
y_axis = df_pca['Component 2']
sns.scatterplot(data = df_pca, x =x_axis, y =y_axis, hue=df_pca['Cluster'], color = ['red', 'blue'])
plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'o', s = 100, color = ['blue', 'red'])#This plotted the centroids
plt.show()
