import numpy as np
from sklearn.datasets import load_digits
import time

class KNN:
    def __init__(self, k=5):
        self.k = k
        self.y_pred = None
        self.k_nearest_neighbours_new = []


    def calculate_distance_between_two_points(self, point1, point2):
        return np.sqrt(np.sum((point1 - point2) ** 2))

    def calculate_distance_between_two_arrays(self, arr1, arr2):
        if len(arr1) != len(arr2):
            raise Exception("Arrays must be of the same length")
        else:
            return self.calculate_distance_between_two_points(arr1, arr2)
            # distances_list = []
            # for i in range(len(arr1)):
            #     distances_list.append(self.calculate_distance_between_two_points(arr1[i], arr2[i]))
            # return np.sqrt(np.sum(distances_list))


    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train


    def __predict_one(self, x):
        y = None
        distances_list = []
        
        try:
            i = 0
            for row in self.x_train:
                distances_list.append(((self.calculate_distance_between_two_arrays(x, row)), self.y_train[i]))
                i += 1
        except Exception as e:
            print(f'Exeption in __predict_one --->', e)

        # Now we have a list of all distances from our x (picture)
        # We need the K lowest distances from the list
        # distances_list.sort(key=lambda t: t[0])
        # k_nearest_neighbours = distances_list[0:self.k]

        # Now we need to find the most common class in the k nearest neighbours
        # And then return the most common value in the dictionary
        # d = {}
        # for tup in k_nearest_neighbours:
        #     if tup[1] in d.keys():
        #         d[tup[1]] += 1
        #     else:
        #         d[tup[1]] = 1
        # sorted_dict = dict(sorted(d.items(), key=lambda item:item[1]))
        # temp_pred = list(sorted_dict.items())[-1][0]

        for i in range(self.k):
            m = min(distances_list, key=lambda x: x[0])
            self.k_nearest_neighbours_new.append(m[1])
            distances_list.remove(m)
            # if (i + 1) % self.k == 0:
            #     print(self.k_nearest_neighbours_new)
        
        res = max(set(self.k_nearest_neighbours_new), key=self.k_nearest_neighbours_new.count)
        
        self.k_nearest_neighbours_new = []

        return res

    def predict(self, x_test):
        y = []
        for x in x_test:
            y.append(self.__predict_one(x))

        self.y_pred = y

        return y


    def accuracy(self, y_test):
        try:
            # Actuall = y_test
            # Predicted = self.y_pred
            correct = 0
            for i in range(len(y_test)):
                if y_test[i] == self.y_pred[i]:
                    correct += 1
            return correct / len(y_test)
        except Exception as e:
            print(f'Exeption in accuracy --->', e)

knn = KNN(3)

digits = load_digits()

X = digits.data
Y = digits.target

x_train = X[:1400]
y_train = Y[:1400]
x_test = X[1400:]
y_test = Y[1400:]

time_start = time.perf_counter()

knn.fit(x_train, y_train)

knn.predict(x_test)

# print('Prediction --->', knn.predict(x_test))
# print('Actual --->', y_test)

time_end = time.perf_counter()

print("Time to fit the model: {}".format(time_end - time_start))

print("Accuracy: {}".format(knn.accuracy(y_test)))