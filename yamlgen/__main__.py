from .genyaml import GenHelmChartValue
from .util import log
import click


@click.command()
@click.option('--data', '-d',
              help='Supply payload in jsonstring format e.g {"name": "app-1", "version": "v1"} ')
def main(data):
    log('yaml file generator', 'blue')
    gen_yaml = GenHelmChartValue(data)
    gen_yaml.build_yaml()
    click.echo('successfully generate yaml file')
    return log('Success: ->', 'green')


if __name__ == '__main__':
    main(prog_name="yamlgen")
