import numpy as np
from sklearn.datasets import load_digits

class KNN:
    def __init__(self, k=5):
        self.k = k

    def calculate_distance_between_two_points(self, point1, point2):
        return np.sum((point1 - point2) ** 2)

    def calculate_distance_between_two_arrays(self, arr1, arr2):
        if len(arr1) != len(arr2):
            raise Exception("Arrays must be of the same length")
        else:
            distances_list = []
            for i in range(len(arr1)):
                distances_list.append(self.calculate_distance_between_two_points(arr1[i], arr2[i]))
            return np.sqrt(np.sum(distances_list))


    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x):
        y = None
        distances_list = []
        
        if self.x_train == None:
            raise Exception('Fit the model first!')
        else:
            i = 0
            for row in self.x_train:
                distances_list.append(((self.calculate_distance_between_two_arrays(x, row)), self.y_train[i]))
                i += 1

        # Now we have a list of all distances from our x (picture)
        # We need the K lowest distances from the list
        distances_list.sort(key=lambda t: t[0])
        k_nearest_neighbours = distances_list[0:self.k]

        # Now we need to find the most common class in the k nearest neighbours
        d = {}
        for tup in k_nearest_neighbours:
            if tup[1] in d.keys():
                d[tup[1]] += 1
            else:
                d[tup[1]] = 1

        # Return the most common value in the dictionary
        # sorted_dict = {}
        # sorted_keys = sorted(d, key=d.get)

        # for w in sorted_keys:
        #     sorted_dict[w] = d[w]
        sorted_dict = dict(sorted(d.items(), key=lambda item:item[1]))

        return list(sorted_dict.items())[-1][0]



knn = KNN(3)

X = 0
pic1 = [0,0,0,30,45,87,0,0,0]
pic2 = [0,0,0,43,90,65,0,0,0]
pic3 = [0,0,0,0,0,0,0,0,0]
pic4 = [0,0,0,0,33,56,0,0,0]
pic5 = [0,0,0,0,0,0,0,0,0]
X = [pic1, pic2, pic3, pic4, pic5]
Y = [1,2,'num 3',4,'num 3']

knn.fit(X, Y)
print('Prediction --->', knn.predict(pic5))