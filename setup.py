from distutils.core import setup
from setuptools import find_packages

setup(
    name = "snowflake",
    version="0.1",
    author ="Jan - DSSS",
    packages=find_packages(),
    install_required=["numpy","turtles","random"]
)