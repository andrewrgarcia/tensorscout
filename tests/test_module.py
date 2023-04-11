import tensorscout as scout
import numpy as np
import matplotlib.pyplot as plt
from timethis import timethis


def make_histograms(data,results, title):
   plt.figure()
   plt.title(title+' N = 100,000')
   plt.hist(data,bins = 7, alpha=0.5,label='data')
   plt.hist(results,bins=600,alpha=0.5,color='magenta',label='data resampling')
   plt.legend()



def test_multicarlo():
    print()
    data = np.random.normal(0, 1, 1000)

    title = 'data resampling (with @multicarlo -- 4 cores)'
    with timethis(title):
        @scout.multicarlo(num_iters=100000, num_cores=4)
        def monte_carlo_function(data, *args, **kwargs):
            simulated_data = np.random.normal(np.mean(data), np.std(data))
            return simulated_data

        results = monte_carlo_function(data)
        print('number unique results: {}/{}'.format(len(np.unique(results)),len(results)))

        make_histograms(data,results,title)

    print('...........................................................')
    title='data resampling (bare)'
    with timethis(title):

        def monte_carlo_function_bare(data, *args, **kwargs):
            simulated_data = np.random.normal(np.mean(data), np.std(data))
            return simulated_data

        results = [monte_carlo_function_bare(data) for i in range(100000)]
        print('number unique results: {}/{}'.format(len(np.unique(results)),len(results)))
        make_histograms(data,results,title)

    plt.show()


def test_campfire():

    def unique(key='x'): return len(np.unique(map[key]))

    with timethis("campfire dictionary"):

        @scout.campfire(num_iters=8, num_cores=4)
        def simulation(data):
            for i in range(1000):
                'the above 1,000 iters is to stress-test  the campfire method against the bare (no multiproc) method (in the end, only the last samples from x y and z are returned)'
                x = [np.random.normal(0, 1) for i in range(5)]
                y = [np.random.normal(0, 1) for i in range(5)]
                z = [np.random.normal(0, 1) for i in range(5)]
        
            # print(data)
            return {'x': [x], 'y': [y], 'z': [z]}

        data = 'c'
        map = simulation(data)
        print(map)
        # print(map.keys())
        print('unique samples -- x: {}, y: {}, z: {}'.format(unique('x'),unique('y'),unique('z')) )  



    print('...................................................')

    with timethis("bare dictionary"):

        def simulation_bare(data, num_iters):
            X,Y,Z = [],[],[]
            for j in range(num_iters):
                for i in range(1000):
                    x = [np.random.normal(0, 1) for i in range(5)]
                    y = [np.random.normal(0, 1) for i in range(5)]
                    z = [np.random.normal(0, 1) for i in range(5)]
                X.extend(x), Y.extend(y), Z.extend(z)

            # print(data)
            return {'x': X, 'y': Y, 'z': Z}

        data = 100
        map_bare = simulation_bare(data, num_iters=400)
        # print(map_bare)
        # print(map_bare.keys())  
        print('unique samples -- x: {}, y: {}, z: {}'.format(unique('x'),unique('y'),unique('z')) )  



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

