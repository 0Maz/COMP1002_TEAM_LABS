import numpy as np

emptyArray = np.empty(int(input("Enter the size of the array: ")))
existingArray = np.array([1, 2, 3, 4, 5])

emptyArray += existingArray

print("Empty array after adding existing array:", emptyArray)