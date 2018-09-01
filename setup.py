#from distutils.core import setup
#from setuptools.config import read_configuration
from setuptools import setup

   
setup(
    name='SchemerFuzzer',
    version='0.0.1',
    author='Stephan van Ellewee',
    author_email='stephan.van.ellewee+schmrfzr@gmail.com',
    packages=['schemerfuzzer'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Does randomized data that follows a given json schema.',
    long_description=open('README.txt').read(),
    install_requires=[
        "jsonschema",
        "sre_yield==1.0.1",
    ],
    dependency_links=[
        "git+https://github.com/svanellewee/sre_yield.git@master#egg=sre_yield-1.0.1",
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
    ],
    aliases={
        "test": "pytest"
    }
)
