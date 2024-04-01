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