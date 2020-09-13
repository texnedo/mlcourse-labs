import numpy as np
import matplotlib as plt


def main():
    arr = np.array([[1,2,4], [3,4,5]])
    print(arr)
    arr1 = arr.transpose()
    print(arr1)


if __name__ == '__main__':
    main()