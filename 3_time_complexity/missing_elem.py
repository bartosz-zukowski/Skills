"""
find missing element
array contains elements from 1 to n+1
one element is missing
"""

def solution(A):
  correct_sum = (len(A)+1)*(len(A) + 2) // 2
  arr_sum = sum(A)
  return correct_sum - arr_sum

print(solution([2,3,1,5]))

"""
tape equilibrium
"""

def solution(A):
  # znajdz najmniejsza roznice pomiedzy podtablicami
  roznice = []
  for p in range (1, len(A), 1):
    roznice.append(abs(sum(A[:p]) - sum(A[p:])))    
  #print(roznice)
  return min(roznice)

print(solution([3,1,2,4,3]))

def clean_solution(A):
  total_sum = sum(A)
  left = 0
  roznice = []
  for p in range(0, len(A) - 1):
    left += A[p]
    roznice.append(abs(left - (total_sum - left)))
  return min(roznice)

print(clean_solution([3,1,2,4,3]))
