from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
    
setup(
    name="mimdb-beta",
    version="0.0.1",
    author="Mostafa Motahari",
    author_email="motahari903@gmail.com",
    description="A full python database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MostafaMim04/MimDB-Beta",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
