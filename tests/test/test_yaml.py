from pprint import pprint

from tests.data.templates import GOOGLE_TEMPLATE
from utils import converter


def test_yaml(yaml_dir):
    converter.list_to_yaml(GOOGLE_TEMPLATE, 'file.yml')
    pprint(converter.yaml_to_list('file.yml'))
