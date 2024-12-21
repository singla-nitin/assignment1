import numpy as np

#a)

array1=np.array([10,52,62,16,16,54,453])

sorted_array=np.sort(array1)
print("Sorted array:")
print(sorted_array)

sorted_indices=np.argsort(array1)
print("\nIndices of the sorted array:")
print(sorted_indices)

smallest_elements=np.sort(array1)[:4]
print("\n4 smallest elements:")
print(smallest_elements)

largest_elements=np.sort(array1)[-5:]
print("\n5 largest elements:")
print(largest_elements)

#b)

array2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_elements = array2[array2 == array2.astype(int)]
float_elements = array2[array2 != array2.astype(int)]
print("\nInteger elements only:")
print(integer_elements)
print("\nFloat elements only:")
print(float_elements)