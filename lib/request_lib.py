# -*- coding: utf-8 -*- 

########################
### BUILD-IN IMPORTS ###
import requests
import json
import time
import logging
import sys
import re

#########################
### FRAMEWORK IMPORTS ###
import lib.common_lib as common_lib

##########################
######   SETTINGS   ######
sys.dont_write_bytecode = True # Disable .pyc file generation
logging.basicConfig(format='%(message)s',level=logging.INFO)


class Request(object):
    @classmethod
    def __print_string_or_json(cls, content):
        if content:
            try:
                json_content = json.loads(content)
                json_content = json.dumps(json_content, sort_keys=True, indent=4, separators=(',', ': '))
                print("---- JSON ----")
                print(json_content)
            except Exception as ex:
                print("Json loads failed")
                print("Exception: " + str(ex))
                print("\n---- Row Body ----")
                print(content)
                print("\n")
        else:
            print("\n---- Body is Empty ----\n")

    @classmethod
    def send_request(cls, method, url, headers, body, params, auth, print_body, redirects, timeout):
        print("\n########################################################")
        print("#######################  REQUEST  ###################### ")
        auth_origin = auth
        url_origin = url
        if params:
            url = method + ' ' + url + '?' + ''.join('{}={}&'.format(k, v) for k, v in params.items())
            url = url[:-1]  + ' HTTP/1.1' # Remove the last & symbol
        else:
            url = method + ' ' + url + ' HTTP/1.1'

        if auth:
            auth = 'Auth: ' + ''.join('{}, {}'.format(auth[0], auth[1]))
        else:
            auth = 'No Auth'
        
        request = ('{}\n{}\n{}\n{}\n{}\n'.format(
            url,
            auth,
            '',
            '======== REQUEST HEADERS ========',
            '\n'.join('{}: {}'.format(k, v) for k, v in headers.items()),
        ))
        print(request)
        if print_body:
            print("======== REQUEST BODY ========")
            Request.__print_string_or_json(body)

        response = requests.request(method=method, url=url_origin, headers=headers, data=body, params=params, auth=auth_origin, timeout=timeout, allow_redirects=redirects)

        print("\n##############################################################")
        print("##########################  RESPONSE  ######################## ")
        response_format = ('\n{}\n{}\n{}'.format(
            '======== RESPONSE HEADERS ========\n',
            'HTTP/1.1 ' + str(response.status_code) + ' ' + response.reason,
            '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        ))
        print(response_format)

        if print_body:
            print('\n======== RESPONSE BODY ========')
            Request.__print_string_or_json(response.content)

        print("ELAPSED TIME: " + str(round(response.elapsed.total_seconds(), 3)))
        print("########################   END   ###################### ")
        print("#######################################################")
        return (response, response.content)

    @classmethod
    def GET(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=15):
        return Request.send_request('GET', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def POST(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=15):
        return Request.send_request('POST', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def HEAD(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('HEAD', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def PUT(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('PUT', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def DELETE(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('DELETE', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def COPY(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('COPY', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def PATCH(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('PATCH', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def MOVE(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('MOVE', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def INIT(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('INIT', url, headers, body, params, auth, print_body, redirects, timeout)

    @classmethod
    def ADD(cls, url, headers=None, body=None, params=None, auth=None, print_body=True, redirects=True, timeout=60):
        return Request.send_request('ADD', url, headers, body, params, auth, print_body, redirects, timeout)