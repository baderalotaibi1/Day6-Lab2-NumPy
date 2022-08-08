import numpy as np
sequence=np.linspace(0,10,15)
print("Q2: Generate a sequence of 15 floats using linspace() function\n",sequence)
arr1=np.arange(1.1,13.1)
arr1=arr1.reshape(2,2,3)
print("Q3: Create a 3-D array in shape (2, 2, 3) containing the four arrays given below\n",arr1)
print("Q4: Print the following:\n","Array's type.\n",type(arr1),"\n",
      "Array's elements datatype.\n",arr1.dtype,"\n"
      "Array's shape.\n",arr1.shape,"\n",
      "Array's size. \n",arr1.size,"\n",
      "Array's dimention.\n",arr1.ndim)
arr1_4D=arr1.reshape(2,2,1,3)
print("Q5: Change the array dimention from 3-D to 4-D\n",arr1_4D.ndim,"\n",arr1_4D.shape)
arr1_4D_int=arr1_4D.astype(int)
print("Q5: Change the array dimention from 3-D to 4-D\n",arr1_4D_int)
for x in np.nditer(arr1_4D_int):
    print(x,end=" ")
print('\nQ8: Print number 8 using array slicing\n',arr1_4D_int[1,0,0,1])

print('\nQ9: Print number 5 and number 6 using array slicing\n',arr1_4D_int[0,1,0,1],arr1_4D_int[0,1,0,2],"\n")

print("Q10: Search for number 8 using where()\n",np.where(arr1_4D_int==8),"\n")
arr1_3D_int=arr1_4D_int.reshape(3,2,2)
print("Q11: Reshape the array as the following\n",arr1_3D_int.shape,"\n")
arr1 = np.array([['A', 'B'], ['E', 'F']])
arr2 = np.array([['C', 'D'], ['G', 'H']])
arrNew=np.vstack((arr1,arr2))
print("Q12.1: Join the arrays without specifying the axis\n",arrNew,"\n")
arrNew=np.concatenate((arr1,arr2),axis=1)
print("Q12.2: Join the arrays along rows with axis = 1\n",arrNew,"\n")
[a,b]=np.split(arrNew,2,axis=1)
print("Q13: Split the array into two arrays with axis = 1, each array should contain four arrays\n","\n")
print(a,"\n")
print(b,"\n")






