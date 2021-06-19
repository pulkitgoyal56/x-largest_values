---
author: Pulkit Goyal
date: May 11, 2021
---

# X LARGEST VALUES

> Problem Statement - [./docs/Data_Coding_Challenge.pdf](./docs/Data_Coding_Challenge.pdf)  

---

1. [Conceptual Overview](#conceptual-overview)
2. [Technical Overview](#technical-overview)
3. [Running](#running)
   1. [Install Requirements](#install-requirements)
   2. [Execute](#execute)
4. [Testing](#testing)

---

## Conceptual Overview

This problem is perfectly solved with a priority queue, which is a data structure that attaches a priority to every element and serves them in increasing (or decreasing) priority. Priority queues are implemented using heaps. The relevant time complexities of heaps using binary trees are as follows -

- **Inserting** a new element in a heap (of size *n*) takes *O(log(n))* time
- **Finding** the lowest (or highest) priority element takes *O(1)* time
- **Creating** a heap out of an unsorted list (of size *n*) takes *O(n)* time

---

## Technical Overview

The presented solution (in Python) uses the `heapq` module of the Python Standard Library to implement the priority queue using binary heaps.  

The worst case performance of the algorithm is as follows:

1. Time Complexity - `O((N-X).log(X))`
1. Space Complexity - `O(X)`

where,

- `X` - Number of elements to be found
- `N` - Size of the input data

---

## Running

### Install Requirements

- *Unix-like* OS
- `python3`

> This program was developed in Python3.8 on MacOS

### Execute

There are two options to pass the data stream to be processed to this program,

1. Pass the file path (relative or absolute) as an argument

    ``` bash
    python3 heapx.py X file
    ```

1. Pass the data via *stdin*

    ``` bash
    # Use the shell redirection operator '<'
    python3 heapx.py X <file
    ```

    or

    ``` bash
    # Pipe it
    cat file | python3 heapx.py X
    ```

where,

- `X` - Number of elements to be found
- `file` - Name of the file containing the data

---

## Testing

I ran all the different permutations of sample data provided in the problem statement through my script (with *X = 3*), and compared it against the expected output.  

> This test is written in the `test.py` file. The sample data with the solution is stored under the `\data` folder.  

Use the following command to run the tests,

``` bash
python3 -m unittest test
```
