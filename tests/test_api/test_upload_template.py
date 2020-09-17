"""
Test of deleting template file
"""

import hamcrest as hc

from tests.data.templates import google
from utils.api_requests import send_request


def test_upload_template(yaml_dir, put_template):
    """
    Delete template file
    """

    get_request = send_request()
    hc.assert_that(
        actual=get_request,
        matcher=hc.has_value([google.tmpl_id])
    )
