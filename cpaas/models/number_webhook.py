# coding: utf-8

"""
    cpaas api

    # Overview  mGage CPaaS API lets you interact with the CPaaS platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  CPaaS APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible. Major releases are not, please be careful when upgrading.  A new account is pinned to the latest version at the time of first request. By default every request sent CPaaS is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  CPaaS also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official CPaaS HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Response format  All CPaaS APIs follow a common response format. Each response will have a `meta` field which contains metadata about the response (like the request_uuid).  APIs which return a single object will have a field `data` which contains the object being returned.  APIs which return a list of objects will have a field `objects` which contains the list of objects being returned.  ## Pagination Pagination for list APIs are controlled using query parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  These fields are also present in the response under the field `meta`. 

    OpenAPI spec version: 1.0
    Contact: apiteam@mgageindia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NumberWebhook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'webhook_id': 'str'
    }

    attribute_map = {
        'webhook_id': 'webhook_id'
    }

    def __init__(self, webhook_id=None):
        """
        NumberWebhook - a model defined in Swagger
        """

        self._webhook_id = None

        if webhook_id is not None:
          self.webhook_id = webhook_id

    @property
    def webhook_id(self):
        """
        Gets the webhook_id of this NumberWebhook.

        :return: The webhook_id of this NumberWebhook.
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """
        Sets the webhook_id of this NumberWebhook.

        :param webhook_id: The webhook_id of this NumberWebhook.
        :type: str
        """

        self._webhook_id = webhook_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NumberWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
