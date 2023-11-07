def cart(lst,s):
  res = []
  for elem in lst:
    for c in s:
      res.append(elem+c)
  return res

def product(s,n):
  res = list(s) # list of operators
  for _ in range(n-1):
    res = cart(res,s)
  return res

def interleave(s1,s2):
  res = ''
  for i in range(min(len(s1),len(s2))):
    res += s1[i]+s2[i]
  return res

def equal_to(lhs,rhs,ops):
  res = set()
  op  = product(f'{ops} ', len(lhs)-1)
  exprs = map(lambda ops: interleave(lhs[:-1],ops) + lhs[-1], op)
  for expr in exprs:
    if eval(expr.replace(' ','')) == rhs:
      res |= {f'{expr.replace(" ","")}={rhs}'}
  return res
