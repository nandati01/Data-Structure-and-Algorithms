# Arrays and Strings

An array is a collection of items stored at the contiguous memory locations. The idea is to store multiple items of the same type together in one place. In C, an array has a fixed size, i.e, it can neither be shrinked nor expanded. This is because the memory for the array is allocated at compile time based on the specified size. Once the memory is allocated, it cannot be resized dynamically.

However, in Python, lists and arrays are used interchangeably. Lists are dynamic arrays that can store elements of different data types and can be resized dynamically. Initializing an array is as easy as ```arr = []```. However, resizing arrays usually involves allocating new, larger array, copying the existing elements into it, and deallocating the old array, which can be inefficient in terms of time and memory.

String is a sequence of characters used to represent text. In Python, strings are immutable (cannot be changed), while in C, they are mutable (can be changed). If we have a mutable array ```arr = ['a', 'b', 'c']```, we can easily replace a character by doing ```arr[0] = 'd'```. However, if we had a string ```s = 'abc'```, we cannot simply do ```s[0]='d'```. With such a small string, we could easily replace the string with ```s = 'dbc'```, but if we were to deal with a larger string, it would be quite expensive.

## Complexity of Some Array and String Operations

| Operation                         | Array | String    |
| :---------------------------------|:------|:----------|
| Appending                         | *O(1) | O(n)      |
| Popping                           | O(1)  | O(n)      |
| Inserting                         | O(n)  | O(n)      |
| Deleting                          | O(n)  | O(n)      |
| Modifying an element              | O(1)  | O(n)      |
| Random Access                     | O(1)  | O(1)      |
| Checking to see if element exists | O(n)  | O(n)      |

_* Appending to the arrays is ammortized O(1). Meaning, on average, the time taken to append an element to the array remains constant regardless of the size of the array. If the array has sufficient capacity to accomodate the new element, the element is added to the end of the array in constant time. However, if the array needs to be resized, a new, larger array is allocated, and the existing elements are copied to the new array. This operation is more expensive, as it requires copying all existing elements to the new array._

# Two Pointers

Two pointers is a common technique used to solve array and string problems. It involves having using two indexes or pointers to traverse the data structure concurrently, often from different starting positions. 

Here is a brief overview of how the two pointers approach works:

- **Two Pointers**: You have two pointers that are initialized to different positions within the array or the string
- **Traversal**: You traverse the data structure using the two pointers, either simultaneously or with one pointer moving ahead of the other
- **Operation**: At each step, you compare the elements pointed to by the two pointers, or perform some operation based on their values.
- **Adjustment of Pointer**: Depending on the problem requirements, you may need to adjust the position of the pointers based on the comparison results or the problem constraints.
- **Termination Condition**: The traversal continues until a certain condition is met, such as reaching the end of the data structure, or satisfying the specific condition specified by the problem. 

## Different Ways to Implement Two Pointers
**Start the pointers at the edge of the input and move them towards each other until they meet**. Below is the algorithm for this idea:

1. Start one pointer at the first index and the other pointer at the last index
2. Use a while loop until the pointers overlap
3. At each iteration, move the left pointer towards the right and the right pointer towards the left. 

Here is the pseudocode for this concept:

```
function fn(arr):
    left, right = 0, arr.length - 1

    while left < right:
        Perform an operation based on the problem requirement
        left ++
        right --
```

Using this method, we will never have a complexity more than *O(n)* for the while loop becuase the pointers start n distance away from each other and move a step closer every time. 

**Move the pointers along both inputs simultaneously until all elements have been traversed**. Below is the algorithm for this idea:

1. Create two pointers, both starting at the first index.
2. Use a while loop until one pointer reaches the end of its iterable
3. At each iteration, increment either one of the pointers or both the pointers forward depending on the problem requirement.
4. The while loop will stop once either one of the pointers reach the end. 

Here is the pseudocode for this concept:
```
function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length
        Do some operation depending on the problem requirement
        i++ or j++ or both

    // To make sure both the iterables are exhausted
    // One of the loops need to run
    while i < arr1.length:
        Do some operation depending on the problem requirement
        i++

    While j < arr2.length:
        Do some operation depending on the problem requirement
        j++
```

This approach will have a time complexity of *O(n+m)* if the work inside the while loop is O(1), where n and m are the lengths of the arrays. At every iteration, we move at least one of the pointers and the loop ends once either one of the pointers reach the end of the iterables. Hence, the pointers cannot move more than ```n + m``` times. 

# Subarrays

Subarrays, also known as contiguous subsequence is a sequence of elements within an array that forms a contiguous portion of the original array. In other words, subarray is a slice or a subset of elements taken from the original array, in a contiguous manner, preserving the order of elements. 

Given an array ```arr``` of length n, a subarray is any sequence of elements arr[i:j] where 0 <= i <= j <= n. An empty array is also considered a subarray. The starting index i is also known as the left bound and the ending index, j is referred to as the right bound. 

# Sliding Window Approach
The sliding window approach is suitable for solving problems that involve finding or optimizing properties of subarrays. Here are a  few scenarios for when this technique can be useful:

1. When the problem involves finding or optimizing properties of subarrays, such as finding the longest subarray, the shortest subarray, the number of subarrays, etc.
2. When the problem involves finding or optimizing properties of subarrays within certain constraint and condition. For example: finding a subarray with a sum greater than or equal to 48. Another example could be finding the longest subarray with the sum of all elements less than or equal to a certain value. 

## Way to Implement Sliding Window

The sliding window only considers valid subarrays - subarrays that satisfy the problem constraint. We initialize two pointers for the sliding window - the left bound of the subarray and the right bound of it. Initially, both the left and the right are at the first index of the array. As long as the right pointer is within the bounds of the array, we increment the right pointer, which is we add more elements to the window. If the window does not satisfy the problem constraint, we move the left pointer forward, shrinking the window. If the subarray or the window is valid, then we only increment the right pointer. 

**For Example**: Given an array, arr, and a target sum, k, find the longest subarray whose sum is smaller than or equal to k. Let ```arr = [2, 4, 3, 7, 6, 2, 1, 3]``` and ```k = 7```.

Here is a breakdown of how the algorithm will work:

1. Initially, ```left = right = 0```. Our window will have ```[2]```
2. ```left = 0```, ```right = 1```. Our window will have ```[2, 4]``` and it is still valid
3. ```left = 0```, ```right = 2```. Window: ```[2, 4, 3]``` and it's invalid
4. ```left = 1```, ```right = 3```. Window: ```[4, 3, 7]``` and it's invalid
5. ```left = 2```, ```right = 4```. Window: ```[3, 7, 6]``` and it's invalid
6. ```left = 3```, ```right = 5```. Window: ```[7, 6, 2]``` and it's invalid
7. ```left = 4```, ```right = 6```. Window: ```[6, 2, 1]``` and it's invalid
8. ```left = 5```, ```right = 7```. Window: ```[2, 1, 3]``` and it's valid

Here is a pseudocode for this algorithm:
```
function fn(arr, k):
    left = right = 0
    window_sum = 0
    max_length = 0
    for right in range(arr.length):
        window_sum += arr[right]

        while window_sum > k:
            window_sum -= arr[left]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length
```

If the array has a length of n, it can have an empty array as its subarray, it can have n subarrays of length 1, n-1 subarrays of length 2, n-2 subarrays of length 3, ... and 1 array of length n. Therefore, there are ```(n^2 + n)/2``` subarrays. Because we are using two pointers, and both the pointers can only move n times, the time complexity for this approach will be O(2n), if the logic can be performed in O(1). 