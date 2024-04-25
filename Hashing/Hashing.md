# Hashing

Hashing is a data structure that stores data in such a way that it can be easily accessed and updated. A hash function deteministically converts an input into an integer. These inputs are called keys and the integers are the indeces of the hash table. The integers must be less than a fixed size set by the programmer. The hash map key must be immutable. Below is an example of a hash algorithm:
1. Let's assign a -> 1, b -> 2, ... z -> 26. 
2. Let the numerical value for combined characters be the sum of the characters. For instance, ab -> 3, cd -> 7, efg -> 18
3. Let's assume that we have a table of size 7. The hash function would be given by ```sum(string) % 7```
4. So we will then store
   - ab -> 3 % 7 = 3
   - cd -> 7 % 7 = 0
   - efg -> 18 % 7 = 4

In an aray, we can easily access and modify elements at any given index since they provide O(1) random access. However, in an array, the indices must be an integer. Hash functions address this limitation by converting any input into an integer. Hash function in combination with an array creates hash table, also known as hash map. A hash table maps keys to values, whereas an array maps indeces to values. Hash tables can add, check, remove, and update elements in O(1) time. Hash maps are unordered data structure, meaning the insertion order does not matter. 

In Python, a dictionary is a type of hash map. Since arrays are mutable and a requirement for hash map key is that it has to be immutable, we can use ```tuple(arr)``` in Python. Another way is to conbert the array into a string. For example. [1, 2, 3] -> "1,2,3". 

## Hash Tables VS Arrays

All of the following operations have a O(1) time complexity for a hash map:
- Inserting element and associating it with a value
- Deleting an element if it exists
- Searching for an element

We can find length, update values, and traverse a hash map with the same time complexity as an array. Moreover, hash maps offer greater convenience in handling sizes; there’s no need to predefine the maximum size of keys because they are converted to integers within certain size limit.

However, for a smaller input size, hash maps tend to be slower due to overhead. This is because every key needs to go through the hash function. Additionally, resizing a hash table is not as simple as resizing an array. When it comes to resizing a hash table, every single key needs to rehashed. And if we choose to use a significantly larger array to begin with, it might result in a waste of space. 

Another major disadvantage with hash maps are **collisions**. When different keys get hashed into a same slot, it is called a collision. If we don't handle collisions well, we might override the data. However, handling collisions slows down the overall speed of the hash table. 

One of the ways of handling collisions is **chaining**. The idea behind chaining is to make each cell of the hash table point to a linked list, which stores both the key and the value. To access one of the key-value pairs, we have to traverse through linked list until the key matches. 

To minimize collisions, it is important that the size of the hash table and modulus are both prime numbers. Some common prime numbers used are:
- 10,007
- 1,000,000,007

## Sets
Sets are data structure similar to hash tables. It also hashes keys into integers. However, those keys are not mapped in sets like they are in hash tables. If you only care about checking to see if an element exists, it would be convenient to use sets. The time complexity for inserting, deleting, and searching an element is O(1). 

Sets don't track frequency. If you have a set and add the same element 100 times, the first operation will add, but the next 99 would do nothing.

## Checking for Existence

One of the most common applications of a hash table or a set is to see if an element exists or not in O(1). Since an array needs O(n) time to do this, using a hash map can improve the complexity from O(n^2) to O(n). 

## Counting

Counting is a very common pattern in hash maps. By "counting", we are referring to tracking the frequency of things. When looking at sliding windows, some problems had constraint as limiting the amount of a certain element in the window. For example, finding the longest substring with at most k 0s. In those problems, we used an integer varraible "curr_window" since we only cared about 0. A hash map opens the door to solving problems where the constraint involves multiple elements. 