"""
Wrapper over the requests module
"""

import json
from typing import Optional
import urllib3

import hamcrest as hc
import requests

import settings


urllib3.disable_warnings()


def send_request(
    method: str = 'get',
    url: str = f"{settings.URL}{settings.API_HANDLER}",
    data: Optional[dict] = None,
    files = None,
) -> str:
    """
    Send API-request to service
    :param method: request method: GET, POST, PUT or DELETE
    :param url: request url
    :param data: POST- or PUT-request data
    :param files: POST- or PUT-request files
    """

    method = method.lower()

    if method not in ('get', 'post', 'put', 'delete'):
        raise ValueError(f'Unsupported method "{method}"')

    response = getattr(requests, method)(
        url=url,
        data={'data': json.dumps(data)} if data else None,
        files={'file': files} if files else None
    )

    hc.assert_that(
        actual=response.status_code,
        matcher=hc.any_of(
            hc.equal_to(200),
            hc.equal_to(201)
        ),
        reason=f"response = {response.content}; status_code = {response.status_code}"
    )

    return response.json()
