# TensorScout
A Python library for tensor operations powered by parallel processing.

<img src="https://raw.githubusercontent.com/andrewrgarcia/tensorscout/main/tensorscout.svg" width="400">


## Installation

```ruby
pip install tensorscout
```

## Contributors

- [Andrew Garcia](https://github.com/andrewrgarcia) - creator and maintainer

## Contributing

1. Fork it (<https://github.com/your-github-user/tensorscout/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Usage Example

```ruby
import tensorscout as scout
import matplotlib.pyplot as plt

'''Performance comparison of a perforation algorithm using a single core (CPU) v. four cores in parallel'''  
def perforate(tensor):
    
    for i in range(10000):
        cds = np.argwhere(tensor!=0)
        tensor[tuple(cds[np.random.randint(cds.shape[0])])] = 0 
    
    return tensor

def perforateMP(tensor):
    cores = 4
    for i in range(int(10000/cores)):
        cds = np.argwhere(tensor!=0)
        tensor[tuple(cds[np.random.randint(cds.shape[0])])] = 0 
    
    return tensor


'''single processor (CPU)'''
A = np.ones((240,240))
A = perforate(A)
plt.imshow(A)

#%timeit perforate(np.ones((240,240)))
#5.23 s ± 9.99 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


'''parallel processing (4 CPUs)'''
A_MP = np.ones((240,240))
A_MP =  scout.rebuild(scout.multi_core(A_MP, perforateMP, cores = 4))
plt.imshow(A_MP)

#%timeit scout.rebuild(scout.multi_core(np.ones((240,240)), perforateMP, cores = 4))
#745 ms ± 8.86 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
