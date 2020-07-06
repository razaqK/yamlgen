import yaml
import json
from .util import log, validate_yaml


class GenHelmChartValue:

    def __init__(self, data):
        self.data = json.loads(data)

    def build_yaml(self):
        try:
            response = yaml.dump(self.data, default_flow_style=False, sort_keys=False)
            is_valid, contents = validate_yaml(response)

            if not is_valid:
                log('Error occurred: -> yaml contents validation failed.', 'red')
                raise Exception('Error occurred: -> yaml contents validation failed.')

            build_policy = open('values.yaml', 'w')
            build_policy.write(contents)
            build_policy.close()
            return log('Success: ->' + json.dumps(contents), 'green')
        except Exception as e:
            log('Error occurred: -> {}'.format(e), 'red')
            raise Exception('Error occurred: -> {}'.format(e))
