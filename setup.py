from setuptools import setup, find_packages

setup(
    name="mylib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy"],  # Add other dependencies if needed
    description="A library for reading grid data",
    author="prathamesh",
    author_email="prathamesh.ratnaparkhi@iucaa.in",
)

