# Match Statements

# REST APIs
# HTTP Status Codes
# 200 = OK , 404 = Not Found , 500 = Internal Server Error , 401 = Unauthorized , OTHERS

def response_code_test(response_code):
    match response_code:
        case 200:
            print('OK')
        case 404:
            print('Not Found')
        case 500:
            print("Internal Server Error")
        case 401:
            print("Unauthorized")
        case _:
            print("Unknown")

response_code_test(200)
response_code_test(500)
response_code_test(499)

# def response_code_test(response_code):
#     if response_code == 200:
#         print('OK')
#     elif response_code == 404:
#         print('Not Found')
#     elif response_code == 500:
#         print("Internal Server Error")
#     elif response_code == 401:
#         print("Unauthorized")
#     else:
#         print("Unknown")
#
# response_code_test(200)
# response_code_test(500)
# response_code_test(499)
