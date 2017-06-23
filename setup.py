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
