from utils.api_requests import send_request


def test_test():

    payload = {
        'tmpl_id': 'autotest_id_1'
    }

    files = open('./temp_file.yaml', 'rb')

    send_request(
        method='put',
        data=payload,
        files=files
    )

    response = send_request()
    print(f"\nResponse: {response}\n")
