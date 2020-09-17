from pprint import pprint

import settings
from tests.data.templates import google
from utils import converter


def teest_yaml(yaml_dir):
    converter.list_to_yaml(google.tmpl_data, f'{settings.YAML_DIR}/file.yml')
    pprint(converter.yaml_to_list(f'{settings.YAML_DIR}/file.yml'))
