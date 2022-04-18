
def pow(val: float, exp: int):
  res = float(1)
  for _ in range(exp):
    res *= val
  return res

'''
double the value c
maintain the property that d_low/c <= B/(P*A) <= d_high/c
'''
def update_exp_numerators(c, d_low, P, A, B):
  c *= 2
  d_low *= 2
  if c*B > (d_low + 1)*P*A:
    d_low += 1
  
  return c, d_low

'''
The goal is calculating (a / (a + m))**(P*A/B)
'''
def exp_calculation(P: int, A: int, B: int, a: int, m: int):

  '''
  because in Decimal calculation, a, m are actually big integers
  we want to find an n, that (a / (a + m))**(P*A/B) = a/(a + n)
  this is equivalent to: ((a + m)/a)**(P*A) = ((a + n)/a)**B
  '''
  c = int(2)
  while (c*B < P*A):
    c *= 2

  d = int(0)
  while (c*B > d*P*A and c*B > (d + 1)*P*A):
    d += 1

  '''
  at first, we find c = 2^k, 
  d_low and d_high, with d_high = d_low + 1, and d_low/c < B/(P*A) < d_high/c
  '''
  d_low = d
  d_high = d + 1

  '''
  n is the target for binary search, we find an initial range of n
  '''
  n_low = int(0)
  n_high = int((float(1 + m/a)**c - 1)/d_low*a + 1) # take upper bound

  while True:
    # print("exp", c, d_low, d_high)
    # print("n", n_low, n_high)
    if n_low + 1 >= n_high:
      return n_low
    
    n_mid = int((n_high + n_low)/2)

    left = pow(float(1 + m/a), c)
    right_low = pow(float(1 + n_mid/a), d_low)
    right_high = pow(float(1 + n_mid/a), d_high)

    if right_low < left and right_high > left:
      c, d_low = update_exp_numerators(c, d_low, P, A, B)
      d_high = d_low + 1
      continue

    if right_low < left:
      n_low = n_mid
    else:
      n_high = n_mid

print(exp_calculation(P=101, A=2, B=199, a=20000000, m=1000000))


