import time

def rec_counter(n, i=0, i_sum=0):
    if i < n:
        i_sum += i
        rec_counter(n, i+1, i_sum)
    else:
        print(' result:', i_sum)

def iter_counter(n):
    i_sum = 0
    for i in range(0, n):
        i_sum += i
    print(' result:', i_sum);

# Recursion
begin = time.time()
print('\nUsing Recursion')
rec_counter(100)
end = time.time()
rec_time = end - begin
print('  tempo:', rec_time)

# Iteration
begin = time.time()
print('\nUsing iteration')
iter_counter(100)
end = time.time()
iter_time = end - begin
print('  tempo:', iter_time)


# Comparison
diff = rec_time - iter_time
if diff < 0:
    diff *= -1

print('\n* Diferença de tempo:', diff)
