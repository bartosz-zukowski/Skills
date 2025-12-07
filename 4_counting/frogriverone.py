def counting(X, A):
  # zbuduj most z paneli od 1 do X
  # zaba chce dojsc na X + 1
  # A to os czasu - indeks to to sekunda
  # Wartosc A[K] = to miesce gdzie spada lisc w tej sekundzie
  # znajdz moment w czasie - indeks, w ktorym bedziesz posiadac komplet liczb od 1 do X
  # X = 5 czyli trzeba skompletowac od 1 do 5
  
  expected_sum = X*(X+1) // 2
  bridge = set()
  for index in range(0, len(A)):
    bridge.add(A[index])
    if expected_sum == sum(bridge):
      return index
  else:
    return -1

print(counting(5, [1, 3, 1, 4, 2, 3, 5, 4]))


def clean_solution(X, A):
  bridge = set()
  for index in range(0, len(A)):
    bridge.add(A[index])
    if len(bridge) == X:
      return index
  return -1

print(clean_solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))



"""
Permcheck - if contains all numbers from 1 to n
"""

def is_permutation(A):
  check_sum = (len(A))*(len(A)+1) // 2
  print(check_sum)
  if sum(A) == check_sum:
    return 1
  return 0

print(is_permutation([4,1,3,2]))


def clean_solution(A):
  check_sum = (len(A))*(len(A)+1) // 2
  # make sure there are no duplicates
  A_set = set(A)
  if sum(A_set) == check_sum and len(A_set) == len(A):
    return 1
  return 0

print(clean_solution([4,1,3,2]))


def best_solution(A):
  A_set = set(A)
  N = len(A)
  # sprawdz czy sa duplikaty
  if len(A_set) != N:
    return 0
  # sprawdz czy najwieksza to N
  if max(A_set) != N:
    return 0
  # jesli przejdzie oba warunki to permutacja
  return 1

print(best_solution([4,1,3,2]))