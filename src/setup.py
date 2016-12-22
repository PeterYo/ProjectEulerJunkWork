__author__ = "ComPeter"
__date__ = "$Dec 10, 2016 9:46:45 AM$"

from setuptools import setup, find_packages

setup (
       name='EulerStuff',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='ComPeter',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )