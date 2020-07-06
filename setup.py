from setuptools import setup, find_packages

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yamlgen",
    version="1.0.0",
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
