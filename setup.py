from setuptools import setup, find_packages

setup(
    name="global-resources",  # The package name users will import
    version="0.1.0",
    description="A collection of Python libraries for various utilities",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # Finds all packages (including python-libs)
    install_requires=[],  # Specify dependencies if necessary
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
