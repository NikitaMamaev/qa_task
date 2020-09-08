

from utils.api_requests import send_request


def test_test():
    response = send_request()
    print(f"\nResponse: {response}\n")
