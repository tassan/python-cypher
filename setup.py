# -*- coding: utf8 -*-

# learn more [github]

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='python-cypher',
    version='0.0.1',
    description='encryption of text using caesars cypher',
    long_description=readme,
    author='Flávio Tassan',
    author_email='ftassan@outlook.com',
    url='https://github.com/tassan/python-cypher',
    #license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)