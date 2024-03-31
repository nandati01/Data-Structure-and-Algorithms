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