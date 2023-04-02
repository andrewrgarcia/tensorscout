import tensorscout as scout
import numpy as np
import matplotlib.pyplot as plt
from timethis import timethis

def test_multicarlo():
    @scout.multicarlo(num_iters=1000, num_cores=4)
    def monte_carlo_function(data, *args, **kwargs):
        simulated_data = np.random.normal(np.mean(data), np.std(data))
        return simulated_data

    data = np.random.normal(0, 1, 1000)
    results = monte_carlo_function(data)
    plt.hist(data,alpha=0.5)
    plt.hist(results,alpha=0.5)
    plt.show()


def test_cakerun():
    matrix = np.ones((252,252))

    plt.imshow(matrix,cmap='bone')
    plt.title('initial canvas')


    num_iters = 10000

    def draw(result):
        plt.figure()
        plt.title('{} -- $N_{{perforated}}$ = {}'.format(title, np.multiply(*result.shape) - np.count_nonzero(result)))
        plt.imshow(result,cmap='bone')
        

    title = 'cakerun MP (4 cores)'
    with timethis("{}".format(title)):

        cores = 4
        @scout.cakerun(num_cores=cores, L_sectors=2)
        def perforate(sector):
            
            for i in range(num_iters // cores):
                cds = np.argwhere(sector!=0)
                sector[tuple(cds[np.random.randint(cds.shape[0])])] = 0 
            return sector

        result = perforate(matrix)
        draw(result)




    title = 'single core'
    with timethis("{}".format(title)):

        def perforate_bare(sector):
            for i in range(num_iters):
                cds = np.argwhere(sector!=0)
                sector[tuple(cds[np.random.randint(cds.shape[0])])] = 0 
            return sector


        result = perforate_bare(matrix)
        draw(result)


    plt.show()

