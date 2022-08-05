import matplotlib.pylab as plt


def read_from_file():
    max_arr, min_arr, avg_arr = [], [], []
    with open("points.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line_arr = line.split(" ")
        max_arr.append(int(line_arr[0]))
        min_arr.append(int(line_arr[1]))
        avg_arr.append(float(line_arr[2][: -1]))

    return max_arr, min_arr, avg_arr


if __name__ == "__main__":
    max_arr, avg_arr, min_arr = read_from_file()
    plt.plot(max_arr, color='b', label="max fitness value")
    plt.plot(avg_arr, color='r', label="average fitness value")
    plt.plot(min_arr, color='g', label="min fitness value")

    plt.xlabel("Generation Number")
    plt.ylabel("Fitness Value")
    plt.legend()
    plt.show()