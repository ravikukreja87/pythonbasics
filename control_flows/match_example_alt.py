# REST APIs
# HTTP Status Codes
# 200, 201, 202 = OK | 404 = Not Found | 500, 501, 502 = Internal Server Error | 401 = Unauthorized | OTHERS


def response_code_test(response_code):
    if response_code == 200 or response_code == 201 or response_code == 202:
        print(f'For {response_code} OK')
    elif response_code == 404:
        print('Not Found')
    elif response_code == 500 or response_code == 501 or response_code == 502:
        print(f"For {response_code} Internal Server Error")
    elif response_code == 401:
        print("Unauthorized")
    else:
        print("Unknown")


response_code_test(200)
response_code_test(202)
response_code_test(500)
response_code_test(501)
response_code_test(499)
