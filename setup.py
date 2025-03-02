from setuptools import setup, find_packages

setup(
    name="movie-language-model",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A project to scrape and analyze movie scripts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/movie-language-model",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4 >=4.13.3, <5.0.0",
        "pandas >=2.2.3, <3.0.0",
        "requests >=2.32.3, <3.0.0",
        "setuptools >=75.8.2, <76.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)