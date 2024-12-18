from setuptools import setup, find_packages

setup(
    name="furniture_assembly",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "networkx>=2.6.3",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for optimizing furniture assembly with human-robot collaboration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/furniture-assembly",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
