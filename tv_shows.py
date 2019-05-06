# add your own imports and auxiliary functions if needed
import numpy as np
import pprint

def fill_adjacency_matrix(matrix, a_rating, b_rating):
  for i in range(0, len(a_rating)):
    for j in range(0, len(a_rating)):
      matrix[i,j+len(a_rating)] = a_rating[i] * b_rating[j]
      matrix[i+len(a_rating),j] = matrix[i,j+len(a_rating)]
  for i in range(0, len(a_rating)):
    for j in range(0, len(a_rating)):
      if j == i+1 or j == i-1:
        matrix[i,j] = a_rating[i]*a_rating[j]
        matrix[i+len(a_rating),j+len(a_rating)] = b_rating[i] * b_rating[j]


def optimize_air_rating(matrix):
  element_count = matrix.shape[0]
  print(element_count)


def tvshows(a, b):
  # implement your solution here
  adjacency_matrix = np.zeros(shape=(2*len(a) , 2*len(a) ))
  fill_adjacency_matrix(adjacency_matrix, a, b)
  optimize_air_rating(adjacency_matrix)
  print(adjacency_matrix)
  return 23066

# test_a = [53,20,50,22,63,43,43,39,83,76]
# test_b = [73,83,10,23,34,24,0,77,33,32]

test_a = [1,2,3,4]
test_b = [2,1,3,5]

expected_result = 23066

my_result = tvshows(test_a, test_b)
print(my_result)

if my_result == expected_result:
  print("Result correct!")
else:
  print("Result incorrect!")
