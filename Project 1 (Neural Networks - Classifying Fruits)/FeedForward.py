import math
import numpy as np
from Loading_Datasets import train_set, test_set

train_set = train_set
test_set = test_set

weight_first_layer = np.random.randn(150, 102)
weight_second_layer = np.random.randn(60, 150)
weight_third_layer = np.random.randn(4, 60)

bias_first_layer = np.zeros((150, 1))
bias_second_layer = np.zeros((60, 1))
bias_third_layer = np.zeros((4, 1))

learning_rate = 1
number_of_epochs = 10
batch_size = 10

train_set = train_set[0:200]


def sigmoid(x):
    result = 1 / (1 + np.exp(-x))
    return result


correct = 0
total = 0
for image in train_set:
    input_image_local = image[0]
    output_label_local = image[1]

    z1 = (weight_first_layer @ input_image_local) + bias_first_layer
    a1 = sigmoid(z1)
    z2 = weight_second_layer @ a1 + bias_second_layer
    a2 = sigmoid(z2)
    z3 = weight_third_layer @ a2 + bias_third_layer
    a3 = sigmoid(z3)

    total += 1
    if np.argmax(a3) == np.argmax(output_label_local):
        correct += 1

print(f"Number of correct prediction is : {correct}")
print(f"Number of total images is : {total}")
print(f"Accuracy is : {float('{:.2f}'.format((correct/total)*100))}%")
