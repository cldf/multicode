from setuptools import setup, find_packages


def read(fname):
    with open(fname) as fp:
        return fp.read().split('\n\n\n')[0]


setup(
    name='multicode',
    version='0.1.1',
    author='Johann-Mattis List',
    description='A python package to help avoid pitfalls when using unicode for linguistic data.',
    long_description=read("README.rst"),
    license="Apache 2",
    url="https://github.com/clpn/multicode",
    packages=find_packages(),
    install_requires=[
        'six',
        'clldutils>=1.12.7',
    ],
    tests_require=['nose', 'coverage', 'mock'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    # entry_points={
    #    'console_scripts' : ['stdb=multicode.cli:main'],
    # },
)
