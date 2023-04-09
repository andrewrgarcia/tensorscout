import tensorscout as scout
import numpy as np
import matplotlib.pyplot as plt
from timethis import timethis

def tecst_multicarlo():
    @scout.multicarlo(num_iters=1000, num_cores=4)
    def monte_carlo_function(data, *args, **kwargs):
        simulated_data = np.random.normal(np.mean(data), np.std(data))
        return simulated_data

    data = np.random.normal(0, 1, 1000)
    results = monte_carlo_function(data)
    plt.hist(data,alpha=0.5)
    plt.hist(results,alpha=0.5)
    plt.show()



def test_campfire():

    with timethis("campfire dictionary"):

        @scout.campfire(num_iters=400, num_cores=4)
        def simulate_data(data, num_iters):
            for i in range(1000):
                'the above 1,000 iters is to stress-test  the campfire method against the bare (no multiproc) method (in the end, only the last samples from x y and z are returned)'
                x = [np.random.normal(0, 1) for i in range(num_iters)]
                y = [np.random.normal(0, 1) for i in range(num_iters)]
                z = [np.random.normal(0, 1) for i in range(num_iters)]
            return {'x': x, 'y': y, 'z': z}

        data = {'data': None}
        
        results = simulate_data(data, num_iters=1)
        results = results["data"]

        map = {key: [] for key in ['x','y','z']}
        for i in results:
            for key in i.keys():
                map[key].append(i[key][0])

        print(map.keys())
        print(len(map['x']))


    with timethis("bare dictionary"):

        def simulate_data_bare(data, num_iters):
            for i in range(1000):
                x = [np.random.normal(0, 1) for i in range(num_iters)]
                y = [np.random.normal(0, 1) for i in range(num_iters)]
                z = [np.random.normal(0, 1) for i in range(num_iters)]
            return {'x': x, 'y': y, 'z': z}

        data = 'hot-dog'
        results = simulate_data_bare(data, num_iters=400)
        print(results.keys())  
        print(len(results['x']))  


def tecst_cakerun():
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

