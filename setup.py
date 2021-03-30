from setuptools import setup, find_packages
import os


version = os.environ.get('version', None)

try:
    with open("Readme.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = "[yamlgen][pypi-url] is an utility ```python``` library on [PyPI][pypi-url]. It's a yaml " \
                       "generator. It convert jsonstring to yaml file. "

setup(
    name="yamlgen",
    version=version,
    author="Razaq Kloc",
    author_email="razaqkor@gmail.com",
    description="A package to generate yaml file. Convert Json String to Yaml",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razaqK/yamlgen",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'yamlgen = yamlgen.__main__:main'
        ]
    },
    install_requires=[
        'click==7.1.1',
        'colorama==0.4.3',
        'pyfiglet==0.8.post1',
        'PyYAML==5.3.1',
        'six==1.14.0',
        'termcolor==1.1.0'
    ]
)
