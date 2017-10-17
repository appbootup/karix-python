# coding: utf-8

"""
    cpaas api

    # Overview  mGage CPaaS API lets you interact with the CPaaS platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  CPaaS APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible. Major releases are not, please be careful when upgrading.  A new account is pinned to the latest version at the time of first request. By default every request sent CPaaS is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  CPaaS also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official CPaaS HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Response format  All CPaaS APIs follow a common response format. Each response will have a `meta` field which contains metadata about the response (like the request_uuid).  APIs which return a single object will have a field `data` which contains the object being returned.  APIs which return a list of objects will have a field `objects` which contains the list of objects being returned.  ## Pagination Pagination for list APIs are controlled using query parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  These fields are also present in the response under the field `meta`. 

    OpenAPI spec version: 1.0
    Contact: apiteam@mgageindia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PhonenumberApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def phonenumber_get(self, **kwargs):
        """
        Query for phone numbers in our inventory.
        Query for phone numbers in our inventory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.phonenumber_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param str country: Filter by country ISO
        :param str pattern: Filter by number pattern
        :param str number_type: Filter by number type; fixed, mobile, tollfree
        :param list[str] service: Filter by service; voice, sms
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.phonenumber_get_with_http_info(**kwargs)
        else:
            (data) = self.phonenumber_get_with_http_info(**kwargs)
            return data

    def phonenumber_get_with_http_info(self, **kwargs):
        """
        Query for phone numbers in our inventory.
        Query for phone numbers in our inventory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.phonenumber_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param str country: Filter by country ISO
        :param str pattern: Filter by number pattern
        :param str number_type: Filter by number type; fixed, mobile, tollfree
        :param list[str] service: Filter by service; voice, sms
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'country', 'pattern', 'number_type', 'service', 'offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phonenumber_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))
        if 'pattern' in params:
            query_params.append(('pattern', params['pattern']))
        if 'number_type' in params:
            query_params.append(('number_type', params['number_type']))
        if 'service' in params:
            query_params.append(('service', params['service']))
            collection_formats['service'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/phonenumber/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2008',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def phonenumber_num_post(self, num, **kwargs):
        """
        Buy number from inventory
        Buy a number from inventory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.phonenumber_num_post(num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int num: Number which you want to buy (required)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param NumberWebhook webhook: Webhook object
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.phonenumber_num_post_with_http_info(num, **kwargs)
        else:
            (data) = self.phonenumber_num_post_with_http_info(num, **kwargs)
            return data

    def phonenumber_num_post_with_http_info(self, num, **kwargs):
        """
        Buy number from inventory
        Buy a number from inventory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.phonenumber_num_post_with_http_info(num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int num: Number which you want to buy (required)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param NumberWebhook webhook: Webhook object
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['num', 'api_version', 'webhook']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phonenumber_num_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'num' is set
        if ('num' not in params) or (params['num'] is None):
            raise ValueError("Missing the required parameter `num` when calling `phonenumber_num_post`")


        collection_formats = {}

        path_params = {}
        if 'num' in params:
            path_params['num'] = params['num']

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook' in params:
            body_params = params['webhook']
        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/phonenumber/{num}/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2012',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
