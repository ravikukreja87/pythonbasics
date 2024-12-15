# Match Statements

# REST APIs
# HTTP Status Codes
# 200, 201, 202 = OK | 404 = Not Found | 500, 501, 502 = Internal Server Error | 401 = Unauthorized | OTHERS

def response_code_test(response_code):
    match response_code:
        case 200 | 201 | 202:
            print(f'For {response_code} - OK')
        case 404:
            print('Not Found')
        case 500 | 501 | 502:
            print(f'For {response_code} - Internal Server Error')
        case 401:
            print("Unauthorized")
        case _:
            print("Unknown")


response_code_test(200)
response_code_test(201)
response_code_test(500)
response_code_test(502)
response_code_test(499)
