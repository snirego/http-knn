import numpy as np

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

    # def predict(self, x_test):
    #     for matrix in 


knn = KNN(3)

list1 = [1,2]
list2 = [0,0]

print(knn.calculate_distance_between_two_arrays(list1,list2))