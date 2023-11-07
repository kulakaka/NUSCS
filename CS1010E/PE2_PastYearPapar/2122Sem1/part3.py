def sum_of_3(L, n):
    # Convert the input tuple to a list to make it mutable
    L = list(L)
    L.sort()  # Sort the list in ascending order

    for i in range(len(L) - 2):
        left, right = i + 1, len(L) - 1

        while left < right:
            current_sum = L[i] + L[left] + L[right]

            if current_sum == n:
                return True
            elif current_sum < n:
                left += 1
            else:
                right -= 1

    return False

print(sum_of_3(tuple(range(1,4000)),11995))




