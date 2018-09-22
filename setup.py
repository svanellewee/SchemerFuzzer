from setuptools import setup

with open("./schemerfuzzer/version", "r") as version_file:
    version = version_file.read()

setup(
    name='SchemerFuzzer',
    version=version,
    author='Stephan van Ellewee',
    author_email='stephan.van.ellewee+schmrfzr@gmail.com',
    packages=['schemerfuzzer'],
    url='https://github.com/svanellewee/SchemerFuzzer',
    license='LICENSE.txt',
    description='Does randomized data that follows a given json schema.',
    long_description=open('README.rst').read(),
    package_data={'': 'version'},
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
    },
    entry_points={
        "console_scripts": [
            'schmrfzzr=schemerfuzzer.bin:main',
        ]
    }
)
