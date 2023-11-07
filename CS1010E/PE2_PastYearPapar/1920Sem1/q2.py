class PizzaShop():
  def __init__(self, pos, name, radius, hour_s, hour_e):
    self.pos    = pos
    self.name   = name
    self.radius = radius
    self.hour_s = hour_s
    self.hour_e = hour_e
  def distance_square_to(self, i, j):
    di, dj = self.pos[0]-i, self.pos[1]-j
    return di*di + dj*dj
  

  
def pd_map(r, c, all_shops, hour):
  m = [[' ']*c for _ in range(r)]
  for i in range(r):
    for j in range(c):
      val,dist = '.',r*r+c*c+1
      for shop in all_shops:
        if shop.hour_s <= hour < shop.hour_e:
          s_dist = shop.distance_square_to(i,j)
          if s_dist <= shop.radius**2:
            if s_dist == dist:
              val = 'X'
            if s_dist < dist:
              val,dist = shop.name[0],s_dist
      m[i][j] = val
  return m
