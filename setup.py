from setuptools import find_packages, setup

setup(name='tensorscout',
      version='1.0',
      description='A python library for straightforward tensor operations',
      url='https://github.com/andrewrgarcia/tensorscout',
      author='Andrew Garcia, PhD',
      license='MIT',
      packages=find_packages(include=['tensorscout']),
      zip_safe=False)
