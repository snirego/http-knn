from turtle import distance
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
            print('Arr1 shape:', arr1.shape)
            print('Arr2 shape:', arr2.shape)
            raise Exception("Arrays must be of the same length")
        else:
            return self.calculate_distance_between_two_points(arr1, arr2)


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
        
        if len(distances_list) != 0:
            for i in range(self.k):
                m = min(distances_list, key=lambda x: x[0])
                self.k_nearest_neighbours_new.append(m[1])
                distances_list.remove(m)
            
            # res = max(set(self.k_nearest_neighbours_new), key=self.k_nearest_neighbours_new.count)

            # print(f'k_nearest_neighbours_new --->', self.k_nearest_neighbours_new)
            knn_list = []
            for i in self.k_nearest_neighbours_new:
                # convert each numpy.ndarray to int
                i = int(i)
                # print('Type i --->', type(i))
                # print(f'i --->', i)
                knn_list.append(i)

            res = max(set(knn_list), key=knn_list.count)
        
        else:
            res = None
        
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
            correct = 0
            for i in range(len(y_test)):
                if y_test[i] == self.y_pred[i]:
                    correct += 1
            return correct / len(y_test)
        except Exception as e:
            print(f'Exeption in accuracy --->', e)