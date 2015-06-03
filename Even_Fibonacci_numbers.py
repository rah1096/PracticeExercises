'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

def even_fib():
    fib_seq = [1, 2]
    result_even = []

    for i in xrange(1, 101):
         len_fib = len(fib_seq)
         fib_seq.append(fib_seq[len_fib - 2] + fib_seq[len_fib - 1])

    for n in fib_seq:
        if n % 2 == 0:
            result_even.append(n)
            if n > 4000000:
                break

    sum_result_even = result_even[:len(result_even) - 1]
    print fib_seq[:10]
    print result_even
    print sum(sum_result_even)


even_fib()
