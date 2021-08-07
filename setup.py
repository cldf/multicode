from setuptools import setup, find_packages


setup(
    name='multicode',
    version='0.2.1',
    author='Johann-Mattis List and Robert Forkel',
    description='A python package to help avoid pitfalls when using unicode for '
                'linguistic data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    url='https://github.com/cldf/multicode',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'multicode=multicode.__main__:main',
        ],
    },
    platforms='any',
    python_requires='>=3.6',
    install_requires=[
        'clldutils>=1.13.10',
        'csvw',
        'segments',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'mock',
            'pytest>=3.6',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
