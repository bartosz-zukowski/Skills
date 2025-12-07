def solution(X, Y, D):
  # start, destination equal or grater, step
  remainder = (Y - X) % D
  if remainder == 0:
    return (Y - X) // D
  else:
    return (Y - X) // D + 1

print(solution(10, 85, 30))

def clean_solution(X, Y, D):
  distance = (Y - X)
  return (distance + D - 1) // D

print(clean_solution(10, 85, 30))