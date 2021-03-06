# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform using an omnichannel messaging API. It also allows you to query your account, set up webhooks and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version releases are backwards compatible but major releases are not, please be careful when upgrading.  Version header `api-version` is used by Karix platform to determine the version of the API request. To use Karix API v2 you can send `api-version` as `\"2.0\"`.  If an API request does not contain `api-version` header then Karix platform uses the pinned API version of the account as the default verison. Your account defaults to the latest API version release at the time of signup. You can check the pinned API version form the [dashboard](https://cloud.karix.io/dashboard).  Karix also provides Helper Libraries for all major languages. Release versions of these libraries correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. Helper libraries are configured to send `api-version` header based on the library version. When using official Karix helper libraries, you dont need to concern yourself with pinned version. Using helper library of latest version will give you access to latest features.  # Supported Channels  Karix omnichannel messaging API supports the following channels:   - sms   - whatsapp  ## SMS Channel To send a message to one or more destinations over SMS channel set `channel` to `sms` in the [Messaging API](#operation/sendMessage).  In trial mode, your account can only send messages to numbers within the sandbox.  ## Whatsapp Channel To send a message to a destination over WhatsApp channel set `channel` to `whatsapp` in the [Messaging API](#operation/sendMessage).  Currently WhatsApp channel can only be used from within the sandbox. Contact [support](mailto:support@karix.io) for an early access outside the sandbox.  Any messages you initiate over WhatsApp to end users must conform to a template configured in WhatsApp. These messages are called \"Notification Messages\". Currently only text messages can be sent as Notification Messages.  Any responses you receive from end users and all replies you send within 24 hours of the last received response are called \"Conversation Messages\".  When using the sandbox for testing and development purposes, we have provided for the following pre-approved templates for \"Notification Messages\":    - Your order * has been dispatched. Please expect delivery by *   - OTP requested by you on * is *   - Thank you for your payment of * * on *. Your transaction ID is *  You can replace `*` with any text of your choice.  Both Notification and Conversation messages are priced differently, please refer to the [pricing page](http://karix.io/messaging/pricing/) for more details.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a resource send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow a common respose structure.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | total         | Total number of objects over all pages    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`  # Events and Webhooks  All asynchronous events generated by Karix platform follow a common structure:  | Key           | Child Key     | Description                                 | |:------------- |:------------- |:------------------------------------------- | | uid           |               | Alphanumeric unique ID of the event         | | api_version   |               | 2.0                                         | | type          |               | Type of the event.                          | | data          |               | Details of the object attached to the event |  Currently implemented event types are:   - `message`: These events are generated when a message is created or       its status is changed. When event `type` is `message` the `data`       parameter contains the Message object (check out the response.data of       [Get Message](#operation/getMessageById) API).     - For outbound messages, `message` events are sent to `events_url` parameter of       [Send Message](#operation/sendMessage) API     - For inbound messages, `message` events are sent to the webhook attached       to the phone number resource using [Edit Number](#tag/Number) API     - For inbound messages to whatsapp sandbox, `message` events are sent to       Webhook URL set on the [Dashboard](https://cloud.karix.io/dashboard/#whatsapp-demo).   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@karix.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from karix.models.create_message_content import CreateMessageContent  # noqa: F401,E501


class CreateMessage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'channel': 'str',
        'source': 'str',
        'destination': 'list[str]',
        'content': 'CreateMessageContent',
        'events_url': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'source': 'source',
        'destination': 'destination',
        'content': 'content',
        'events_url': 'events_url'
    }

    def __init__(self, channel='sms', source=None, destination=None, content=None, events_url=None):  # noqa: E501
        """CreateMessage - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._source = None
        self._destination = None
        self._content = None
        self._events_url = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        self.source = source
        self.destination = destination
        self.content = content
        if events_url is not None:
            self.events_url = events_url

    @property
    def channel(self):
        """Gets the channel of this CreateMessage.  # noqa: E501

        Channel to use to send message over Supported Channels: sms, whatsapp   # noqa: E501

        :return: The channel of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CreateMessage.

        Channel to use to send message over Supported Channels: sms, whatsapp   # noqa: E501

        :param channel: The channel of this CreateMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["sms", "whatsapp"]  # noqa: E501
        if channel not in allowed_values:
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

    @property
    def source(self):
        """Gets the source of this CreateMessage.  # noqa: E501

        Sender ID for the message which will be displayed to the receiver. It should specification E.164 with international calling codes.   - When sending a message to US/Canada, `source` must be a number     which belongs to your Karix Subaccount (or main account).   - When sending a message over `whatsapp` channel, `source` must be the     whatsapp sandbox number from your dashboard or a Whatsapp enabled number     added to your account.   # noqa: E501

        :return: The source of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateMessage.

        Sender ID for the message which will be displayed to the receiver. It should specification E.164 with international calling codes.   - When sending a message to US/Canada, `source` must be a number     which belongs to your Karix Subaccount (or main account).   - When sending a message over `whatsapp` channel, `source` must be the     whatsapp sandbox number from your dashboard or a Whatsapp enabled number     added to your account.   # noqa: E501

        :param source: The source of this CreateMessage.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this CreateMessage.  # noqa: E501

        The destination numbers for the message.   - When sending a message over `whatsapp` channel, the `destination` array     must contain only one phone number.   # noqa: E501

        :return: The destination of this CreateMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CreateMessage.

        The destination numbers for the message.   - When sending a message over `whatsapp` channel, the `destination` array     must contain only one phone number.   # noqa: E501

        :param destination: The destination of this CreateMessage.  # noqa: E501
        :type: list[str]
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def content(self):
        """Gets the content of this CreateMessage.  # noqa: E501


        :return: The content of this CreateMessage.  # noqa: E501
        :rtype: CreateMessageContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateMessage.


        :param content: The content of this CreateMessage.  # noqa: E501
        :type: CreateMessageContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def events_url(self):
        """Gets the events_url of this CreateMessage.  # noqa: E501

        Status change events for the `queued` messages will be sent to `events_url`.   - Please read more about [Karix Events](#section/Events-and-Webhooks) structure.   - A message sent over `whatsapp` channel might generate a `read` event directly     and skip the `delivered` event. A message for which you receive a `read` event     should be considered `delivered` as well.   # noqa: E501

        :return: The events_url of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._events_url

    @events_url.setter
    def events_url(self, events_url):
        """Sets the events_url of this CreateMessage.

        Status change events for the `queued` messages will be sent to `events_url`.   - Please read more about [Karix Events](#section/Events-and-Webhooks) structure.   - A message sent over `whatsapp` channel might generate a `read` event directly     and skip the `delivered` event. A message for which you receive a `read` event     should be considered `delivered` as well.   # noqa: E501

        :param events_url: The events_url of this CreateMessage.  # noqa: E501
        :type: str
        """

        self._events_url = events_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateMessage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
