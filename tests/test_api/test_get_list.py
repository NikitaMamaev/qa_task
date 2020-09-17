"""
Test of getting templates list
"""

import hamcrest as hc

from utils.api_requests import send_request


def test_get_list(yaml_dir):
    """
    Get templates list
    """

    get_request = send_request()
    hc.assert_that(
        actual=get_request,
        matcher=hc.has_key("templates")
    )
