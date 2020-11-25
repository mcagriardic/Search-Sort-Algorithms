import math
steps = 0

def bs(l, val):
  global steps
  steps += 1

  if not l:
    print("Element is not present in the container! Took %s steps..." %steps) 
    steps = 0
    return False

  mid_idx = math.ceil(len(l) / 2) - 1
  mid_val = l[mid_idx]

  if val == mid_val:
    print("Element found! Took %s steps..." %steps)
    steps = 0
    return True

  if val > mid_val:
    return bs(l[mid_idx + 1:], val)
  else:
    return bs(l[:mid_idx + 1], val)

l = [1,4,7,8,9]
bs(l, 1)

# >> Element found! Took 3 steps...

bs(l, 11)

# >> Element is not present in the container! Took 4 steps...