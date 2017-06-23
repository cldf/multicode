from setuptools import setup, find_packages

setup(
    name='multicode',
    version='0.1.0',
    author='Johann-Mattis List',
    license="Apache 2",
    packages=find_packages(),
    install_requires=[
        'six',
        'clldutils>=1.12.7',
    ],
    tests_require=['nose', 'coverage', 'mock'],

    # entry_points={
    #    'console_scripts' : ['stdb=multicode.cli:main'],
    # },
)
