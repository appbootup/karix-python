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


class MessageResponse(object):
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
        'uid': 'str',
        'source': 'str',
        'destination': 'str',
        'status': 'str',
        'text': 'str',
        'queued_time': 'datetime',
        'sent_time': 'datetime',
        'delivered_time': 'datetime',
        'direction': 'str',
        'error_code': 'str',
        'cost': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'source': 'source',
        'destination': 'destination',
        'status': 'status',
        'text': 'text',
        'queued_time': 'queued_time',
        'sent_time': 'sent_time',
        'delivered_time': 'delivered_time',
        'direction': 'direction',
        'error_code': 'error_code',
        'cost': 'cost'
    }

    def __init__(self, uid=None, source=None, destination=None, status=None, text=None, queued_time=None, sent_time=None, delivered_time=None, direction=None, error_code=None, cost=None):
        """
        MessageResponse - a model defined in Swagger
        """

        self._uid = None
        self._source = None
        self._destination = None
        self._status = None
        self._text = None
        self._queued_time = None
        self._sent_time = None
        self._delivered_time = None
        self._direction = None
        self._error_code = None
        self._cost = None

        if uid is not None:
          self.uid = uid
        if source is not None:
          self.source = source
        if destination is not None:
          self.destination = destination
        if status is not None:
          self.status = status
        if text is not None:
          self.text = text
        if queued_time is not None:
          self.queued_time = queued_time
        if sent_time is not None:
          self.sent_time = sent_time
        if delivered_time is not None:
          self.delivered_time = delivered_time
        if direction is not None:
          self.direction = direction
        if error_code is not None:
          self.error_code = error_code
        if cost is not None:
          self.cost = cost

    @property
    def uid(self):
        """
        Gets the uid of this MessageResponse.
        Unique ID for a message sent or received

        :return: The uid of this MessageResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this MessageResponse.
        Unique ID for a message sent or received

        :param uid: The uid of this MessageResponse.
        :type: str
        """

        self._uid = uid

    @property
    def source(self):
        """
        Gets the source of this MessageResponse.
        Sender ID for the message

        :return: The source of this MessageResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this MessageResponse.
        Sender ID for the message

        :param source: The source of this MessageResponse.
        :type: str
        """

        self._source = source

    @property
    def destination(self):
        """
        Gets the destination of this MessageResponse.
        Destination number for the message

        :return: The destination of this MessageResponse.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this MessageResponse.
        Destination number for the message

        :param destination: The destination of this MessageResponse.
        :type: str
        """

        self._destination = destination

    @property
    def status(self):
        """
        Gets the status of this MessageResponse.
        Current status of the message. Possible values: - `queued`: Message has been queued in CPaaS system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that CPaaS failed             to send the message to a carrier.             In case of `inbound` message, this means that CPaaS failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier. 

        :return: The status of this MessageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MessageResponse.
        Current status of the message. Possible values: - `queued`: Message has been queued in CPaaS system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that CPaaS failed             to send the message to a carrier.             In case of `inbound` message, this means that CPaaS failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier. 

        :param status: The status of this MessageResponse.
        :type: str
        """
        allowed_values = ["queued", "sent", "failed", "delivered", "undelivered", "rejected"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def text(self):
        """
        Gets the text of this MessageResponse.

        :return: The text of this MessageResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this MessageResponse.

        :param text: The text of this MessageResponse.
        :type: str
        """

        self._text = text

    @property
    def queued_time(self):
        """
        Gets the queued_time of this MessageResponse.

        :return: The queued_time of this MessageResponse.
        :rtype: datetime
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        """
        Sets the queued_time of this MessageResponse.

        :param queued_time: The queued_time of this MessageResponse.
        :type: datetime
        """

        self._queued_time = queued_time

    @property
    def sent_time(self):
        """
        Gets the sent_time of this MessageResponse.

        :return: The sent_time of this MessageResponse.
        :rtype: datetime
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        """
        Sets the sent_time of this MessageResponse.

        :param sent_time: The sent_time of this MessageResponse.
        :type: datetime
        """

        self._sent_time = sent_time

    @property
    def delivered_time(self):
        """
        Gets the delivered_time of this MessageResponse.

        :return: The delivered_time of this MessageResponse.
        :rtype: datetime
        """
        return self._delivered_time

    @delivered_time.setter
    def delivered_time(self, delivered_time):
        """
        Sets the delivered_time of this MessageResponse.

        :param delivered_time: The delivered_time of this MessageResponse.
        :type: datetime
        """

        self._delivered_time = delivered_time

    @property
    def direction(self):
        """
        Gets the direction of this MessageResponse.

        :return: The direction of this MessageResponse.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this MessageResponse.

        :param direction: The direction of this MessageResponse.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def error_code(self):
        """
        Gets the error_code of this MessageResponse.

        :return: The error_code of this MessageResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this MessageResponse.

        :param error_code: The error_code of this MessageResponse.
        :type: str
        """

        self._error_code = error_code

    @property
    def cost(self):
        """
        Gets the cost of this MessageResponse.

        :return: The cost of this MessageResponse.
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this MessageResponse.

        :param cost: The cost of this MessageResponse.
        :type: str
        """

        self._cost = cost

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
        if not isinstance(other, MessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
