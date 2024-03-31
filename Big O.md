# Introduction To Big O

Big O is a mathematical notation that is used to describe the computational complexity of an algorithm. The computational complexity is divided into two parts:

- **Time Complexity** - Amount of time an algorithm takes to complete as the size of the imput data grows.
- **Space Complexity** - Amount of memory an algorithm uses as the input size increases.

Understanding big O notation is crucial for analyzing the efficiency of algorithms and make informed decision about which algorithm to use in what context. 

## Understanding How Complexity Works
Complexity is described as a limiting behavior of a function as the argument tends towards infinity. The arguments are variables that represent values that change between different inputs, which affect the algorithm. The most common variable used is 'n', which is the length of the input. 

Big O notation expresses the upper bound of the growth rate of a function. Here are some common big O notations and their meanings:

- **O(1) - Constant Time**: The execution time of the algorithm is constant and does not change with the size of the input data set.
- **O(n) - Linear Time**: The execution time grows linearly with the increase in input size. 
- **O(logn) - Logarithmic Time**: The execution time increases logarithmically with the input size. Algorithms with logarithmic time complexity are highly efficient and are often found in operations like binary search.
- **O(nlogn) - Linearithmic Time**: This complexity often occurs in algorithms that break the problem into smaller problems, solve them independently, and combine their results.
- **O(n^2) - Quadratic Time**: The execution time grows quadratically with the input size. Nested loops over the input data typically have this complexity.
- **O(2^n) - Exponential Time**: The execution time doubles with each addition to the input data size. Algorithms with this complexity becomes infeasible to run even with relatively small input size.
- **O(n!) - Factorial Time**: This execution time increases factorially with the input data size. This is often seen in algorithms that generate all possible permutations of a dataset.
- **O(n.m) - Linear Time**: The performance of the algorithm is dependent on two different inputs of size n and m. It is used to represent the complexity of algorithms involving two variables, each contributing linearly to the total complexity.
  
## Rules for Calculating Complexity

The function is used to classify algorithms according to how their run time or space requirements grow as the size of the input increases. Complexity is not meant to be the exact representation of the number of operations. Again, it is meant to describe how the number of changes with the number of inputs. 

For example, let's take a non empty array of positive integers called arr. First, let's write a code to find the largest number in arr.

``` python
max = 0

for num in arr:
    if num > max:
        max = num

print(max)
```
In this example, the time complexity is O(n). The algorithm involves iterating over each element in ```arr ```, so if we define 
*n* as the length of ```arr```, our algorithm uses approximately *n* steps. If we pass an array with a length of 10, it will perform approximately 10 steps. However, if we pass an array with a length of 10,000,000,000, it will perform approximately 10,000,000,000 steps. We could say that for an array of *n* 10, we would need two additional operations; one for initializing max and the other for printing max. However, we usually tend to ignore the constants since we are trying to see how the number of operations changes with the input. 

Another thing to consider is that we calculate the complexity as the variables tend to inifinity. Meaning, we tend to ignore all terms except the most powerful one. In the above example, even though the algorithm requires n + 2 operations, we say that the complexity is O(n) because as n tends to infinity, the constant term is effectively 0 in comparison. Additionally, even if the complexity of an algorithm was *O(n^2 +10n)*, we would say the complexity is *O(n^2)* because n^2 becomes so large, 10n is effectively 0 in comparison. 

## Analyzing Time Complexity
### Example One
``` python
# Given an integer array arr with length n, print each number in the array
for i in arr:
    print(i)
```
The given algorithm has a time complexity of O(n). In each for loop, we are performing a print, which costs O(1). The for loop iterates n times, which gives the total time complexity of *O(1.n)* = *O(n)*. 
### Example Two
``` python
# Given an integer array arr, with length n
for num in arr:
    for i in range(0, 100):
        print(num)
```
The given algorithm also has a time complexity of O(n). The print statement in each for loop costs O(1). Because the for loop iterates a hundred times, the total cost of performing the print statement is O(100). Therefore, the total time complexity for the above algorithm is *O(100n)* = *O(n)*. Even though the first example and this one have the same complexity, this algorithm will be much slower compared to the first one. 
### Example Three
``` python
#Given an array arr, with length n
for i in arr:
    for j in arr:
        print(i * j)
```
The given algorithm has a time complexity of O(n^2). The print operation costs O(1). The inner for loop costs O(n). The outer for loop also costs O(n). Therefore, the total complexity is *O(n.n)* = *O(n^2)*. 
### Example Four
``` python
# Given two arrays arr1 and arr2, with length n and m respectively
for i in arr1:
    print(i)

for j in arr2:
    print(j)
```
The above algorithm has a time complexity of O(n + m). The first loop has a complexity of O(n) and the second loop has a complexity of O(m). 
### Example Five
``` python
#Given an array arr, with length n
for i in range(0, len(arr)):
    for j in range (0, len(arr)):
        print(arr[i] + arr[j])
```
The above algorithm has a time complexity of O(n^2). In this algorithm, for each iteration of the outer loop, the number of iteration for the inner loop decreases. 
    * When i = 0, the inner loop runs n times
    * When i = 1, the inner loop runs n - 1 times
    * ...
    * When i = n -1, the inner loop runs 1 time
The total number of iterations is given by *n(n + 1) / 2* = (n^2 + n) / 2*. Therefore, the complexity is *O((n^2 + n) / 2) = O(n^2)* as the length tends to infinity. 
### Example Six
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```
The above algorithm has a time complexity of *O(2^n)*. In the recursive algorithm, the number of function calls grows exponentially with n. For each call to ```fibonacci(n)```, we make two subsequent calls to ```fibonacci(n-1)``` and ```fibonacci(n-2)```, except for the base cases. 
### Example Seven
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid  # Target found
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    return -1  # Target not found
```
The above algorithm has a time complexity of *O(logn)*. This is because each time the input size is reduced by half. After the first step, we are only considering n/2 elements and after the second, we are considering n/4 and so on. At each step we are reducing our input by 50%.