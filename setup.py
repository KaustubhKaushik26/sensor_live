from setuptools import find_packages,setup
from typing import List



setup(
    name="sensor_live",
    version='0.0.1',
    author='Kaustubh Kaushik',
    author_email='kaustubhkaushik26@gmail.com',
    packages=find_packages(),
    install_requires = ['pymongo']
)