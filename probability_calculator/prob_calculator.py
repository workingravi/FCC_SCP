import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, n):
    if n > len(self.contents):
      return self.contents
    else:
      removed = []
      #balls = copy.copy(self.contents)
      for _ in range(n):
        r = random.randrange(len(self.contents))
        #print("index to remo: ", r)
        removed.append(self.contents.pop(r))
        #print("Remaining:", self.contents)
      return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  m = 0  
  ebl = len(expected_balls)
  #print("EB: ", expected_balls)
    
  for _ in range(num_experiments):
    chat = copy.deepcopy(hat)
    drawn = chat.draw(num_balls_drawn)
    dd = {}
    for item in drawn:
      dd[item] = dd.get(item, 0) + 1
    
    c = 0
    for color, val in expected_balls.items():
      if color not in dd.keys():   
        c = 0
        break
      else:
        if dd[color] < val:
          c = 0
          break
        c += 1
        
      if c == ebl:  #Both conditions work for all colors
        m += 1

  return m/num_experiments

  

