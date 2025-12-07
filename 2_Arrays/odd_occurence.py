"""
Odd OccurrencesInArray
"""

def solution(A):
  occurences = {}
  for item in A:
    if item in occurences:
      occurences[item] += 1
    else:
      occurences[item] = 1
  for key, value in occurences.items():
    if value % 2 != 0:
      return key

print(solution([9, 3, 9, 3, 9, 7, 9]))


"""
Solution XOR ()
"""

def solution_xor(A):
  wynik = 0
  for liczba in A:
    wynik = wynik ^ liczba
  return wynik

print(solution_xor([9, 3, 9, 3, 9, 7, 9]))

def czy_potega_2(n):
  return n > 0 and (n & (n - 1) == 0)

print(czy_potega_2(16))