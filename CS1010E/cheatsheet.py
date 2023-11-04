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
