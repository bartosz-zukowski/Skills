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


"""
missing integer   --- gdy sa ujemne liczby
"""
A = [1, 3, 6, 4, 1, 2]

def missing_integer(A):
  # podziele wzgledem osi na dodatnie i ujemne zbiory
  positive = set()
  negative = set()
  for element in A:
    if element <= 0:
      negative.add(element)
    else:
      positive.add(element)
  # jezeli dodatni jest pusty to zwracam 1, ujemna czesc mnie nie interesuje
  #print(negative)
  #print(positive)
  if not positive:
    return 1
  else:
    check_sum = (len(positive)+1)*(len(positive) + 2) // 2
    positive_sum = sum(positive)
    #print(check_sum)
    #print(positive_sum)
    if positive_sum == check_sum:
      return max(positive) + 1
    else:
      return check_sum - positive_sum 


print(missing_integer(A))
print(missing_integer([1, 2, 3]))
print(missing_integer([-1, -3]))
