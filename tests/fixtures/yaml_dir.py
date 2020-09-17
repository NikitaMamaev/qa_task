"""
Create directory for temporary yaml-files before testing and remove after
"""

import os

import pytest

import settings


def remove_yaml_dir():
    """
    Remove directory for temporary yaml-files
    """

    if os.path.exists(settings.YAML_DIR):
        for yaml_file in os.listdir(settings.YAML_DIR):
            os.unlink(os.path.join(settings.YAML_DIR, yaml_file))

        os.rmdir(settings.YAML_DIR)


@pytest.fixture(scope='session')
def yaml_dir(request):
    """
    Create directory for temporary yaml-files
    """

    if not os.path.exists(settings.YAML_DIR):
        os.mkdir(settings.YAML_DIR)

    request.addfinalizer(remove_yaml_dir)
