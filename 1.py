import numpy as np
arr=np.array([1,2,3,6,4,5])

#a)
print(arr[::-1])

#b)
arr1=np.array([[1,2,3],[2,4,5],[1,2,3]])
arr1=arr1.flatten()
print(arr1)

#c)
arr2=np.array([[1,2],[3,4]])
arr3=np.array([[1,2],[3,4]])
if(arr2.all()==arr3.all()):
    print("Arrays are equal")
else:
    print("Arrays are unequal")

#d)
x=np.array([1,2,3,4,5,1,2,1,1,1])
unique_x,count_x=np.unique(x,return_counts=True)
freq_elements_x= unique_x[np.argmax(count_x)]
index_x=np.where(x==freq_elements_x)[0]
print("Most frequent value in x = ",freq_elements_x,"indices",index_x)

y=np.array([1,1,1,2,3,4,2,4,3,3])
unique_y,count_y=np.unique(y,return_counts=True)
freq_elements_y= unique_y[np.argmax(count_y)]
index_y=np.where(y==freq_elements_y)[0]
print("Most frequent value in y = ",freq_elements_y,"indices",index_y)

#e)
gfg=np.matrix('[4,1,9;12,3,1;4,5,6]')
print("Sum of all elements =",np.sum(gfg))
print("Sum of all elements row wise =",np.sum(gfg,1))
print("Sum of all elements column wise =",np.sum(gfg,0))

#f)
n_array=np.array([[55,25,15],[30,44,2],[11,45,77]])

sum_of_diagonal_elements=np.trace(n_array)
eigen_vectors=np.linalg.eig(n_array)
inverse_matrix=np.linalg.inv(n_array)
determinant=np.linalg.det(n_array)
print(f"Sum of diagonal elements: {sum_of_diagonal_elements}")
print(f"Eigen values and Eigen vectors of the matrix: \n{eigen_vectors}")
print(f"Inverse of the matrix: \n{inverse_matrix}")
print(f"Determinant of the matrix:{determinant}")

#g)
p1=np.array([[1,2],[2,3]])
q1=np.array([[4,5],[6,7]])
product_1=np.dot(p1,q1)
covariance_1=np.cov(p1.flatten(),q1.flatten())
print("Matrix multiplication (1st case):")
print(product_1)
print("\nCovariance between the matrices (1st case):")
print(covariance_1)

p2=np.array([[1,2],[2,3],[4,5]])
q2=np.array([[4,5,1],[6,7,2]])
product_2=np.dot(p2,q2)
covariance_2=np.cov(p2.flatten(),q2.flatten())
print("Matrix multiplication (2nd case):")
print(product_2)
print("\nCovariance between the matrices (2nd case):")
print(covariance_2)

#h)
l=np.array([[2,3,4],[3,2,9]])
m=np.array([[1,5,0],[5,10,3]])

inner_product=np.inner(l,m)
outer_product=np.outer(l,m)
cartesian_product=np.array(np.meshgrid(l.flatten(),m.flatten())).T.reshape(-1,2)
print("Inner product:")
print(inner_product)
print("\nOuter product:")
print(outer_product)
print("\nCartesian product:")
print(cartesian_product)
