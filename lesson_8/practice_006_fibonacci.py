# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7,
# Print out the sequence: 0, 1, 1, 2, 3, 5, 8

n = 10
fib_sequence=[0, 1]
for i in range(2, n):
    next_fib = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_fib)
print(fib_sequence)


n = 10
fib_seq = [0, 1]
for _ in range(n - 2):
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
print(fib_seq)
