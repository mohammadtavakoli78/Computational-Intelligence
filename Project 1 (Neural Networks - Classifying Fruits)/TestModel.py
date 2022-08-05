import math
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from Loading_Datasets import train_set, test_set

input_neurons = 102
first_layer_neurons = 150
second_layer_neurons = 60
third_layer_neurons = 4


def show_cost(step_number, epoch_count, costs):
    plt.title("Cost" + str(step_number))
    x = np.arange(0, epoch_count)
    plt.plot(x, costs)
    path = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(path + f'\cost-step{step_number}.png')
    plt.show()


def sigmoid(x):
    result = 1 / (1 + np.exp(-x))
    return result


def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))


def create_weight_and_bias(input_layer: int, first_layer: int, second_layer: int, third_layer: int):
    w1 = np.random.randn(first_layer, input_layer)
    w2 = np.random.randn(second_layer, first_layer)
    w3 = np.random.randn(third_layer, second_layer)

    b1 = np.zeros((first_layer, 1))
    b2 = np.zeros((second_layer, 1))
    b3 = np.zeros((third_layer, 1))

    return w1, w2, w3, b1, b2, b3


def run_alogrithm(train_set, number_of_images, number_of_epochs, batch_size, weight_first_layer, weight_second_layer,
                  weight_third_layer, bias_first_layer,
                  bias_second_layer, bias_third_layer):
    costs = []

    for i in range(number_of_epochs):
        accuracy = 0
        cost = 0

        random.shuffle(train_set)
        print(f'epoch number : {i}')

        for counter in range(int(number_of_images/batch_size)):

            grad_weight_first_layer = np.zeros((first_layer_neurons, input_neurons))
            grad_weight_second_layer = np.zeros((second_layer_neurons, first_layer_neurons))
            grad_weight_third_layer = np.zeros((third_layer_neurons, second_layer_neurons))

            grad_bias_first_layer = np.zeros((first_layer_neurons, 1))
            grad_bias_second_layer = np.zeros((second_layer_neurons, 1))
            grad_bias_third_layer = np.zeros((third_layer_neurons, 1))

            for image in train_set[counter * 10:(counter + 1) * 10]:
                input_image_local = image[0]
                output_label_local = image[1]
                z1 = weight_first_layer @ input_image_local + bias_first_layer
                a1 = sigmoid(z1)
                z2 = weight_second_layer @ a1 + bias_second_layer
                a2 = sigmoid(z2)
                z3 = weight_third_layer @ a2 + bias_third_layer
                a3 = sigmoid(z3)

                cost += sum(pow((a3 - output_label_local), 2))

                grad_weight_third_layer += (2 * sigmoid_deriv(z3) * (a3 - output_label_local)) @ (np.transpose(a2))
                grad_bias_third_layer += (2 * sigmoid_deriv(z3) * (a3 - output_label_local))

                ga2 = np.zeros((second_layer_neurons, 1))

                ga2 = np.transpose(weight_third_layer) @ (2 * sigmoid_deriv(z3) * (a3 - output_label_local))

                grad_weight_second_layer += (sigmoid_deriv(z2) * ga2) @ (np.transpose(a1))
                grad_bias_second_layer += (sigmoid_deriv(z2) * ga2)

                ga1 = np.zeros((first_layer_neurons, 1))
                ga1 = np.transpose(weight_second_layer) @ (sigmoid_deriv(z2) * ga2)

                grad_weight_first_layer += (sigmoid_deriv(z1) * ga1) @ (np.transpose(input_image_local))
                grad_bias_first_layer += (sigmoid_deriv(z1) * ga1)

                if np.argmax(z3) == np.argmax(output_label_local):
                    accuracy += 1

            weight_first_layer = weight_first_layer - (learning_rate * (grad_weight_first_layer / batch_size))
            weight_second_layer = weight_second_layer - (learning_rate * (grad_weight_second_layer / batch_size))
            weight_third_layer = weight_third_layer - (learning_rate * (grad_weight_third_layer / batch_size))

            bias_first_layer = bias_first_layer - (learning_rate * (grad_bias_first_layer / batch_size))
            bias_second_layer = bias_second_layer - (learning_rate * (grad_bias_second_layer / batch_size))
            bias_third_layer = bias_third_layer - (learning_rate * (grad_bias_third_layer / batch_size))

        costs.append(cost / number_of_images)

    print(f"Number of correct prediction is : {accuracy}")
    print(f"Number of total images is : {number_of_images}")
    print(f"Accuracy is: {(accuracy / number_of_images) * 100}%")
    show_cost(5, number_of_epochs, costs)


if __name__ == "__main__":
    train_set = train_set

    weight_first_layer, weight_second_layer, weight_third_layer, bias_first_layer, \
        bias_second_layer, bias_third_layer = create_weight_and_bias(
            input_layer=input_neurons, first_layer=first_layer_neurons,
            second_layer=second_layer_neurons, third_layer=third_layer_neurons)

    learning_rate = 1
    number_of_epochs = 20
    batch_size = 10

    run_train = 1   # set 0 for test

    if run_train:
        number_of_images = 1900
        train_set = train_set[0:number_of_images]
    else:
        number_of_images = 600
        train_set = test_set[0:number_of_images]

    run_alogrithm(train_set=train_set, number_of_images=number_of_images, number_of_epochs=number_of_epochs,
                  batch_size=batch_size, weight_first_layer=weight_first_layer, weight_second_layer=weight_second_layer,
                  weight_third_layer=weight_third_layer, bias_first_layer=bias_first_layer,
                  bias_second_layer=bias_second_layer, bias_third_layer=bias_third_layer)
