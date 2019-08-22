## too slow for regular runs
if False:
    res = np.zeros(10000)
    for i in range(10000):
        res[i] = min_crib_dist(t3,sub_cipher(t1T,rand_dict()))

    import matplotlib.pyplot as plt
    fig, axis = plt.subplots()
    axis.hist(res)
    fig.savefig("tmp.png")
