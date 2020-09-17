from utils.api_requests import send_request


def teest_put(yaml_dir):

    payload = {
        'tmpl_id': 'test_test'
    }

    files = open('./file.yml', 'rb')

    send_request(
        method='put',
        data=payload,
        files=files
    )

    response = send_request()
    print(f"\nResponse: {response}\n")

    install_request = send_request(
        method='post',
        handler='test_test/install'
    )

    print(f'\nINSTALL:{install_request}\n')

    send_request(
        method='delete',
        handler='test_test'
    )

    response = send_request()
    print(f"\nResponse: {response}\n")
