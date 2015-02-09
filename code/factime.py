import timeit

setup = '''
import factors
import eucalg
'''

t1 = timeit.timeit('factors.common_factors(361,407)',
                    setup = setup, number=10000)
print("brute force ",t1)

t2 = timeit.timeit('eucalg.euc_alg_loop(361,407)',
                    setup = setup, number=10000)
print("looping EA ",t2)

t3 = timeit.timeit('eucalg.euc_alg_rec(361,407)',
                    setup = setup, number=10000)

print("recursive EA ",t3)

t4 = timeit.timeit('factors.common_factors(9874,7573)',
                    setup = setup, number=1000)

print("big brute force",t4)

t5 = timeit.timeit('eucalg.euc_alg_loop(9874,7573)',
                    setup = setup, number=1000)

print("big loop EA",t5)

t6 = timeit.timeit('eucalg.euc_alg_rec(9874,7573)',
                    setup = setup, number=1000)

print("big rec EA",t6)



