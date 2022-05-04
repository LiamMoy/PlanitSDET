# Challenge 1: Get the nth number in the Fibonacci Sequence given n. Alternatively, given a number F, print out whether it's a Fibonacci number and what the closest index n is in the Fibonaci Sequence

# The first part can be done:
# (a) recursively using fib_recursive(n)
# (b) recursively with memoization using fib_recursive_memo(n)
# (c) iteratively via fib_iterative(n)

# The second part can be done using fib_evaluate(F) which could be modified to call any of methods (a)-(c) but uses method (b)

def fib_recursive(n):

    # Validate the input as a non-negative integer

    if not (isinstance(n,int) and n >= 0):
        raise ValueError(f"n must be a non-negative integer")

    # Define the first two numbers in the Fibonacci Sequence; this could alternatively be done as follows:
    # if n in {0, 1}:
    #   return n

    if n == 0:
        return 0

    if n == 1:
        return 1

    # Find the nth number in the Fibonacci Sequence by adding the previous two numbers, which are recursively generated from their two preceding numbers using the same function, etc, back to the first two numbers defined in the base case

    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Define the initial state of the memoization cache as the first two numbers in the sequence

fib_recursive_memo_cache = {0: 0, 1: 1}

def fib_recursive_memo(n):

    # Validate the input as a non-negative integer

    if not (isinstance(n,int) and n >= 0):
        raise ValueError(f"n must be a non-negative integer")

    # If the input is already in the memoization cache, return its value

    if n in fib_recursive_memo_cache:
        return fib_recursive_memo_cache[n]

    # If the input is not already in the memoization cache, calculate its value, add it to the memoization cache, and then return its value

    fib_recursive_memo_cache[n] = fib_recursive_memo(n - 1) + fib_recursive_memo(n - 2)
    return fib_recursive_memo_cache[n]

def fib_iterative(n):

    # Validate the input as a non-negative integer

    if not (isinstance(n,int) and n >= 0):
        raise ValueError(f"n must be a non-negative integer")

    # Define the first two numbers in the Fibonacci Sequence. This could alternatively be done as follows:
    # if n in {0, 1}:
    #   return n

    if n == 0:
        return 0

    if n == 1:
        return 1

    # Define two local variables and initialise them with the first two numbers in the Fibonacci Sequence

    nminusoneth, nth = 0,1

    # Iterate through the Fibonacci Sequence past the input number

    for i in range (2, n + 1):

    # Calculate each Fibonacci number and retain the previous Fibonacci number

        nminusoneth, nth = nth, nminusoneth + nth

    # Return the requested Fibonacci number

    return nth

def fib_evaluate(F):

    # Validate the input as a non-negative integer

    if not (isinstance(F,int) and F >= 0):
        raise ValueError(f"A Fibonacci number can only be a non-negative integer")

    # Define the first two numbers in the Fibonacci Sequence. This could alternatively be done as follows:
    # if F in {0, 1}:
    #   print(F,"is a Fibonacci number")

    if F == 0:
        print("0 is a Fibonacci number with index 1")
        return

    if F == 1:
        print("1 is a Fibonacci number with index 2")
        return

    # Define three variables and initiate them with the value of the first three Fibonacci numbers

    a = 0
    b = 1
    c = 1
    I = 2

    # Step through the Fibonacci Sequence until we reach a Fibonacci number that is equal to or larger than F

    while a < F:
        a = b + c
        c = b
        b = a
        I = I + 1

    # Where F is a Fibonacci number, return the index

    if a == F:
        print(F,"is a Fibonacci number with index",I)
        return

    # Where F is not a Fibonacci number, look at the Fibonacci numbers either side, return those Fibonacci numbers, and return the index of the Fibonacci number that is closer

    else:

        if F - fib_recursive_memo(I - 1) > fib_recursive_memo(I) - F:

                print(F,"is not a Fibonacci number; the nearest Fibonacci numbers are",fib_recursive_memo(I-1),"and",fib_recursive_memo(I),"and the closest index is",I)
                return

        if F - fib_recursive_memo(I - 1) < fib_recursive_memo(I) - F:

                print(F,"is not a Fibonacci number; the nearest Fibonacci numbers are",fib_recursive_memo(I-1),"and",fib_recursive_memo(I),"and the closest index is",I-1)
                return

        if F - fib_recursive_memo(I - 1) == fib_recursive_memo(I) - F:

            print(F,"is not a Fibonacci number; the nearest Fibonacci numbers are",fib_recursive_memo(I-1),"and",fib_recursive_memo(I),"and the closest indices are both",I-1,"and",I,"as the two nearest Fibonacci numbers are equidistant")

        return
    return

# QED
