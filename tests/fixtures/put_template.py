"""
Create temporary file and upload it before testing and delete file after
"""

import os

import pytest

import settings
from tests.data.templates import google
from utils.api_requests import send_request
from utils.converter import list_to_yaml


filepath = f'{settings.YAML_DIR}/{google.filename}'

def remove_template():
    """
    Delete temporary template file
    """

    if os.path.exists(filepath):
        os.remove(filepath)


@pytest.fixture(scope='function')
def put_template(request, yaml_dir):
    """
    Upload template file
    """

    list_to_yaml(google.tmpl_data, filepath)

    files = open(filepath, 'rb')
    payload = {
        'tmpl_id': google.tmpl_id
    }

    send_request(
        method='put',
        data=payload,
        files=files
    )

    request.addfinalizer(remove_template)
