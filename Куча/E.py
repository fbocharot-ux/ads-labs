import heapq

n = int(input())
numbers = [int(x) for x in input().split()]

heapq.heapify(numbers)
total_cost = 0.0
while len(numbers) > 1:
    first = heapq.heappop(numbers)
    second = heapq.heappop(numbers)
    current_sum = first + second
    total_cost += current_sum * 0.05
    heapq.heappush(numbers, current_sum)

print(f"{total_cost:.2f}")
