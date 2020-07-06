
[![PyPI Version][pypi-image]][pypi-project-url]
[![PyPI Version Image][pypi-version-image]][pypi-project-url]

# YamlGen

[yamlgen][pypi-url] is an utility ```python``` library on [PyPI][pypi-url]. It's a yaml generator.
It convert jsonstring to yaml file.

:rotating_light:
## Features



# Installation

Installation is done using the
[`pip install` command](https://pypi.org/project/pip/):
```
   $ pip install yamlgen
   $ pip3 install yamlgen
```

### Usage:

```
Usage: yamlgen [OPTIONS]

Options:

  -d, --data TEXT  Supply payload in jsonstring format e.g
                   {"name": "app-1", "version": "v1"}

  --help           Show this message and exit.
```

```
// Generate svc policy file

yamlgen -d '{"name": "test-app", "image": [{"name": "image-1"}, {"name": "image-2"}]}'
```




[pypi-image]: https://img.shields.io/pypi/v/yamlgen.svg
[pypi-project-url]: https://pypi.org/project/yamlgen
[pypi-version-image]: https://img.shields.io/pypi/pyversions/yamlgen.svg
[pypi-url]: https://pypi.org

