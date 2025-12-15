"""
Znajdź najmniejszą dodatnią liczbę całkowitą (większą od 0), której nie ma w tablicy A.
"""


def solution(A):
  A_set = set(A)
  for i in range(1, len(A) + 2):
    if i not in A_set:
      return i
  return 1

print(solution(A))
print(solution([1, 2, 3]))
print(solution([-1, -3]))