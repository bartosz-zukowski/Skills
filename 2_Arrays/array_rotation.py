"""
Docstring for 2_Arrays.array_rotation
"""

def rotate_array(arr, k):
    pass




"""
Zadanie: Napisz funkcję zamien_krańce(A), która przyjmuje listę, 
zamienia miejscami pierwszy i ostatni element, 
a następnie zwraca zmodyfikowaną listę. Jeśli lista jest pusta lub ma 1 element, zwróć ją bez zmian.
[1, 2, 3, 4, 5] -> powinno zwrócić [5, 2, 3, 4, 1]
"""

def zmien_krance(A):
    if len(A) < 2:
        return A
    A[0], A[-1] = A[-1], A[0]
    return A

print(zmien_krance([1, 2, 3, 4, 5]))  # Output: [5, 2, 3, 4, 1]


"""
Masz tablicę A i liczbę K. Musisz przesunąć elementy tablicy w prawo o K razy. 
Ostatni element wskakuje na pierwsze miejsce (dlatego "cykliczna").
Przykład: Tablica: [3, 8, 9, 7, 6] 
Przesuwamy o 1: [6, 3, 8, 9, 7] (szóstka z końca wskoczyła na początek).
"""

def rotate_array(arr, k):
    if len(arr) < 2:
        return arr
    for _ in range(k):
        last_element = arr.pop()
        arr.insert(0, last_element)
    return arr

print(rotate_array([3, 8, 9, 7, 6], 1))  # Output: [6, 3, 8, 9, 7]

def rotate_array_efficient(arr, k):
    n = len(arr)
    if n < 2:
        return arr
    k = k % n
    return arr[-k:] + arr[:-k]

print(rotate_array_efficient([3, 8, 9, 7, 6], 1))  # Output: [6, 3, 8, 9, 7]

"""
Masz tablicę o parzystej liczbie elementów. 
Twoim zadaniem jest zamienić pierwszą połowę z drugą połową.
Dane: A = [1, 2, 3, 4, 5, 6] Cel: [4, 5, 6, 1, 2, 3]
"""

def zamien_polowy(arr):
  n = len(arr)
  if n < 2:
    return arr
  k = n // 2
  return arr[-k:] + arr[:-k]

print(zamien_polowy([1, 2, 3, 4, 5, 6]))

"""
To klasyk nad klasykami.
Ćwiczenie 3: Odwracanie (Reverse)
Dane: A = [1, 2, 3, 4, 5] Cel: [5, 4, 3, 2, 1]
"""

def odwracanie(arr):
  if len(arr) < 2:
    return arr
  return arr[::-1]




def usun_index(arr, i):
  return arr[::i] + arr[i+1:]

print(usun_index([10, 20, 30, 40, 50], 3))