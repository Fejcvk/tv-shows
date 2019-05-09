# add your own imports and auxiliary functions if needed
import numpy as np
import pprint
import random
import time
dct = {}
def get_max_product(a, b,a_idx = 0, b_idx = 0):
  if a_idx == b_idx == len(a):
    return 0
  v = dct.get((a_idx, b_idx), None)
  if v is not None:
    return v
  r1 = r2 = r3 = 0

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

  val = max(r1,r2,r3)
  dct[(a_idx, b_idx)] = val
  return val  

def get_max_product_dp(a,b):

  result = np.zeros(shape=(len(a)+1,len(a)+1))
  for i in range(0,result.shape[0]):
    for j in range(0, result.shape[1]):
      if i == 0 and j == 0:
        result[i,j] = 0
      elif i == 1 and j == 0:
        result[i, j] = a[i-1]
      elif j == 1 and i == 0:
        result[i,j] = b[j-1]
      elif i == j == 1:
        result[i,j] = a[i-1]*b[j-1]
      else :
        result[i,j] = max (
          result[i-1,j-1] + a[i-1]*b[j-1],
          result[i-2,j] + a[i-2]*a[i-1],
          result[i,j-2] + b[j-2]*b[j-1]
        )
  print(result)
  return result.max
  
def tvshows(a, b):
  # implement your solution here
  # t = get_max_product_dp(a,b)
  return get_max_product(a,b)

test_a = [random.randint(0,100) for i in range(0,500)]
test_b = [random.randint(0,100) for i in range(0,500)]




# test_a = [1,2]
# test_b = [3,4]

expected_result = 23066
start = time.time()
my_result = tvshows(test_a, test_b)
end = time.time()
print(f"Result equal to {my_result} obtained in {end-start} seconds")

if my_result == expected_result:
  print("Result correct!")
else:
  print("Result incorrect!")
