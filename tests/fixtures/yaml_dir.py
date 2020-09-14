"""
Test fixtures
"""

import os

import pytest

from settings import YAML_DIR


def remove_yaml_dir():
    """
    Test fixture finalizer
    """

    if os.path.isdir(YAML_DIR):
        for yaml_file in os.listdir(YAML_DIR):
            os.unlink(os.path.join(YAML_DIR, yaml_file))
        os.rmdir(YAML_DIR)

    print("\n---FINALE!!!---\n")


@pytest.fixture(scope='session')
def yaml_dir(request):
    """
    Test fixture finalizer
    """

    print("\n---BEGIN!!!---\n")
    print(os.path.isdir(YAML_DIR))
    if not os.path.isdir(YAML_DIR):
        os.mkdir(YAML_DIR)


    request.addfinalizer(remove_yaml_dir)
