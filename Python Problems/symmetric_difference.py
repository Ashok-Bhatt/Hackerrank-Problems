a = int(input())
M = set(map(int, input().split()))
b = int(input())
N = set(map(int, input().split()))

new_set = M.symmetric_difference(N)

while new_set:
    minimum = min(new_set)
    print(minimum)
    new_set.remove(minimum)
