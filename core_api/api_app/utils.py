from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 404:
            response.data['detail'] = 'Sorry, this page does not exist'
        elif response.status_code == 403:
            response.data['detail'] = 'Access forbidden'
        elif response.status_code == 401:
            response.data['detail'] = 'You have to be authorized to gain access to this page'
        response.data['status_code'] = response.status_code

    return response
