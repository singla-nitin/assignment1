import numpy as np

#a)

array=np.array([[1,-2,3],[-4,5,-6]])
absolute_values=np.abs(array)
print("Element-wise absolute value:")
print(absolute_values)

percentiles_flattened=np.percentile(array,[25,50,75])
percentiles_columns=np.percentile(array,[25,50,75],axis=0)
percentiles_rows=np.percentile(array,[25,50,75],axis=1)

print("\n25th, 50th, and 75th percentiles of flattened array:")
print(percentiles_flattened)

print("\n25th, 50th, and 75th percentiles for each column:")
print(percentiles_columns)

print("\n25th, 50th, and 75th percentiles for each row:")
print(percentiles_rows)

mean_flattened = np.mean(array)
median_flattened = np.median(array)
std_flattened = np.std(array)

mean_columns = np.mean(array,axis=0)
median_columns = np.median(array,axis=0)
std_columns = np.std(array,axis=0)

mean_rows = np.mean(array,axis=1)
median_rows = np.median(array,axis=1)
std_rows = np.std(array,axis=1)

print("\nMean, Median, and Standard Deviation of flattened array:")
print(f"Mean: {mean_flattened}, Median: {median_flattened}, Std: {std_flattened}")

print("\nMean, Median, and Standard Deviation for each column:")
print(f"Mean: {mean_columns}, Median: {median_columns}, Std: {std_columns}")

print("\nMean, Median, and Standard Deviation for each row:")
print(f"Mean: {mean_rows}, Median: {median_rows}, Std: {std_rows}")

#b)

a=np.array([-1.8,-1.6,-0.5,0.5,1.6,1.8,3.0])
floor_values=np.floor(a)
print("Floor Values:")
print(floor_values)

ceiling_values=np.ceil(a)
print("\nCeiling Values:")
print(ceiling_values)

truncated_values=np.trunc(a)
print("\nTruncated values:")
print(truncated_values)

rounded_values=np.round(a)
print("\nRounded Values:")
print(rounded_values)