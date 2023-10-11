import numpy as np

my_list=list(map(int,input().split()))
my_array = np.array(my_list)
new_array = np.reshape(my_array,(3,3))
print(new_array)
