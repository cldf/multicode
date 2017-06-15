import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages,Extension
# setup package name etc as a default
pkgname = 'multicode'
pkg_dir = {'':'.'}
pkg_location = '.'

setup(
        name=pkgname,
        version='0.1',
        packages=find_packages(pkg_location),
        package_dir=pkg_dir,
        install_requires=['clldutils'],
        #entry_points={
        #    'console_scripts' : ['stdb=multicode.cli:main'],
        #},
        author='Johann-Mattis List'
        )
