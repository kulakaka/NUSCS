fn = lambda x:x**2
print(fn(2))


li = [1,23,4,5,6,654,2]

#remove by value
li.remove()

#remove by index
li.pop()
#or
del li[1]


#produce a list of first 10 squared numbers?
d_li = [i*i for i in range(1,11)]
# set is a an unordered collection with no duplicate elements NO index

setA = {1,2,3,4}
setB = {3,4,5,6}

#Union
setA | setB 

#intersection
setA & setB

#A-B
setA - setB
#(A|B) - A&B
setA ^ setB


with open('','w') as af:
    for i in af


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)



# Define a function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the result to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]

# Use map() with a lambda function to square each number
squared_numbers = map(lambda x: x ** 2, numbers)
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]
