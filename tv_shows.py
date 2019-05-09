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
  size = len(a)+1
  result = np.zeros(shape=(size,size))
  a = np.array(a)
  b = np.array(b)
  for i in range(0,size):
    for j in range(0, size):
      if i < 2 and j < 2:
        if i == j == 0:
          result[i,j] = 0
        elif i-1 > 0 and j-1 > 0:
          result[i-1,j-1] + a[i-1]*b[j-1]
        elif i > j:
          result[i,j] = a[i-1]
        else :
          result[i,j] = b[j-1]
      else :
        r1=r2=r3=0
        if i - 2 >= 0:
          r1 = result[i-2,j] + a[i-2]*a[i-1]
        if j - 2 >= 0:
          r2 = result[i,j-2] + b[j-2]*b[j-1]
        if i-1>=0 and j-1>=0:
          r3=result[i-1,j-1] + a[i-1]*b[j-1]
        result[i,j] = max (
          r3,
          r1,
          r2
        )
  return result[size-1,size-1]
  
def tvshows(a, b):
  # implement your solution here
  dp_time_start = time.time()
  t = get_max_product_dp(a,b)
  dp_time_end = time.time()
  rec_t_start = time.time()
  t2 = 10
  rec_t_end = time.time()
  print(f"From dp = {t} obtained in {dp_time_end - dp_time_start}s , from recursion = {t2} obtained in {rec_t_end - rec_t_start}s")
  return t
test_a = [random.randint(0,100) for i in range(0,5000)]
test_b = [random.randint(0,100) for i in range(0,5000)]




# test_a = [53,20,50,22,63,43,43,39,83,76]
# test_b = [73,83,10,23,34,24,0,77,33,32]

expected_result = 23066
start = time.time()
my_result = tvshows(test_a, test_b)
end = time.time()
print(f"Result equal to {my_result} obtained in {end-start} seconds")

if my_result == expected_result:
  print("Result correct!")
else:
  print("Result incorrect!")
