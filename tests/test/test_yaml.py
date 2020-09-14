from pprint import pprint

from settings import YAML_DIR
from tests.data.templates import GOOGLE_TEMPLATE
from utils import converter


def test_yaml(yaml_dir):
    converter.list_to_yaml(GOOGLE_TEMPLATE, f'{YAML_DIR}/file.yml')
    pprint(converter.yaml_to_list(f'{YAML_DIR}/file.yml'))
