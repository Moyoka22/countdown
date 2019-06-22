import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=" countdown",
    version="0.0.1",
    author="Moyewa Odiase",
    author_email="moyeodiase@hotmail.co.uk",
    description="A simple terminal countdown timer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moyoka22/countdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)