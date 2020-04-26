import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abheyogy", # Replace with your own username
    version="0.0.1",
    author="Pranav Salunke",
    author_email="abheyogy@gmail.com",
    description="A demo Python tool doing basic Configuration Management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abheyogy/netconfigurator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
