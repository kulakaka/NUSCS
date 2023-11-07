

def super_fib_R(term2, n):
    # Base case: If n is 1, return a list with the first term
    if n == 1:
        return [1]
    if n ==2:
        return [1,term2]
    if n ==3:
        return [1,term2,1+term2]
    sfs = super_fib_R(term2,n-1)
    sfs.append(sfs[-1]*2)                   #base on look the pattern of result list
    return sfs



def super_fib_I(term2, upper):
  res = [1]
  while res[-1] <= upper:
    if len(res) == 1:
      res.append(term2)
    elif len(res) == 2:
      res.append(term2+1)
    else:
      res.append(res[-1]*2)
  res.pop()
  return res
print(super_fib_I(4, 100))

def smallest_second(n):
  while n%2 == 0:
    n = n//2
  return n