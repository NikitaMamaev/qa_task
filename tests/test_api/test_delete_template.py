"""
Test of deleting template file
"""

import hamcrest as hc

from tests.data.templates import google
from utils.api_requests import send_request


def test_delete_template(yaml_dir, put_template):
    """
    Delete template file
    """

    send_request(
        method='delete',
        handler=google.tmpl_id
    )

    get_request = send_request()
    hc.assert_that(
        actual=get_request,
        matcher=hc.not_(hc.has_value([google.tmpl_id]))
    )
