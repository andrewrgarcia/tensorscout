from setuptools import find_packages, setup

setup(name='tensorscout',
      version='1.0',
      description='A Python library for multiprocessing-powered tensor operations.',
      url='https://github.com/andrewrgarcia/tensorscout',
      author='Andrew Garcia, PhD',
      license='MIT',
      packages=find_packages(include=['tensorscout']),
      zip_safe=False)
