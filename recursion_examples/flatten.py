def flatten(lst):
  flattened = []

  if not lst:
    return None
  
  for elem in lst:
    if not isinstance(elem, list):
      flattened.append(elem)
    elif isinstance(elem, list):
      flattened.extend(flatten(elem))
  
  return flattened

  flatten([1,2,3,[4,5,[6,7,8]]])