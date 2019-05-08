# add your own imports and auxiliary functions if needed
import numpy as np
import pprint


def get_max_product(a, b,a_idx = 0, b_idx = 0):
  r1 = r2 = r3 = 0

  if a_idx == b_idx == len(a):
    return 0

  if a_idx + 2 <= len(a):
    r1 = a[a_idx]*a[a_idx+1] + get_max_product(a,b,
       a_idx= a_idx + 2,
        b_idx= b_idx)

  if a_idx + 1 <= len(a) and b_idx + 1 <= len(b):
    r2 = a[a_idx]*b[b_idx] + get_max_product(a,b,
      a_idx = a_idx+1,
        b_idx = b_idx+1)

  if b_idx + 2 <= len(a):
    r3 = b[b_idx]*b[b_idx+1] + get_max_product(a,b,
       a_idx= a_idx,
        b_idx= b_idx + 2)

  return max(r1,r2,r3)

def get_max_product_dp(a,b):
  
  matrix = np.zeros(shape=(len(a),len(a)))
  a_idx = 0
  b_idx = 0

  while a_idx <= len(a):
    while b_idx <= len(b):
      r1 = r2 = r3 = 0
      if a_idx + 2 <= len(a):
        r1 = a[a_idx]*a[a_idx-1] + matrix[a_idx-2,b_idx]

      if a_idx + 1 <= len(a) and b_idx + 1 <= len(b):
        r2 = a[a_idx]*b[b_idx] + matrix[a_idx-1, b_idx-1]

      if b_idx + 2 <= len(a):
        r3 = b[b_idx]*b[b_idx-1] + matrix[a_idx,b_idx-2]

      maximum = max(r1,r2,r3)
      matrix[a_idx,b_idx] = maximum
      if r1 == maximum: 
        a_idx+=2
      elif r2 == maximum: 
        a_idx += 1 
        b_idx += 1
      else : 
        b_idx += 2

      print(matrix)
    return matrix.max
  
def tvshows(a, b):
  # implement your solution here
  t = get_max_product_dp(a,b)
  return get_max_product(a,b)

# test_a = [53,20,50,22,63,43,43,39,83,76]
# test_b = [73,83,10,23,34,24,0,77,33,32]




test_a = [1,2]
test_b = [3,4]

expected_result = 23066

my_result = tvshows(test_a, test_b)
print(my_result)

if my_result == expected_result:
  print("Result correct!")
else:
  print("Result incorrect!")
