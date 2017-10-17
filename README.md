# cpaas-python
# Overview  mGage CPaaS API lets you interact with the CPaaS platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  CPaaS APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible. Major releases are not, please be careful when upgrading.  A new account is pinned to the latest version at the time of first request. By default every request sent CPaaS is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  CPaaS also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official CPaaS HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Response format  All CPaaS APIs follow a common response format. Each response will have a `meta` field which contains metadata about the response (like the request_uuid).  APIs which return a single object will have a field `data` which contains the object being returned.  APIs which return a list of objects will have a field `objects` which contains the list of objects being returned.  ## Pagination Pagination for list APIs are controlled using query parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  These fields are also present in the response under the field `meta`. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cpaas 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cpaas
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cpaas
from cpaas.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
cpaas.configuration.username = 'YOUR_USERNAME'
cpaas.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = cpaas.AccountsApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
subaccount = cpaas.CreateAccount() # CreateAccount | Subaccount object (optional)

try:
    # Create a new subaccount
    api_response = api_instance.create_subaccount(api_version=api_version, subaccount=subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_subaccount: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mgageindia.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**create_subaccount**](docs/AccountsApi.md#create_subaccount) | **POST** /accounts/ | Create a new subaccount
*AccountsApi* | [**get_subaccount**](docs/AccountsApi.md#get_subaccount) | **GET** /accounts/ | Get a list of accounts
*AccountsApi* | [**get_subaccount_by_id**](docs/AccountsApi.md#get_subaccount_by_id) | **GET** /accounts/{uid}/ | Get details of an account
*AccountsApi* | [**patch_subaccount**](docs/AccountsApi.md#patch_subaccount) | **PATCH** /accounts/{uid}/ | Edit an account
*MessageApi* | [**get_message**](docs/MessageApi.md#get_message) | **GET** /message/ | Get list of messages sent or received
*MessageApi* | [**get_message_by_id**](docs/MessageApi.md#get_message_by_id) | **GET** /message/{uid}/ | Get message details by id.
*MessageApi* | [**send_message**](docs/MessageApi.md#send_message) | **POST** /message/ | Send a message to a list of phone numbers
*NumberApi* | [**get_number**](docs/NumberApi.md#get_number) | **GET** /number/ | Get details of all phone numbers linked to your account.
*NumberApi* | [**number_num_delete**](docs/NumberApi.md#number_num_delete) | **DELETE** /number/{num}/ | Unrent number from your account
*NumberApi* | [**number_num_get**](docs/NumberApi.md#number_num_get) | **GET** /number/{num}/ | Get details of a number
*NumberApi* | [**number_num_patch**](docs/NumberApi.md#number_num_patch) | **PATCH** /number/{num}/ | Edit phone number belonging to your account
*PhonenumberApi* | [**phonenumber_get**](docs/PhonenumberApi.md#phonenumber_get) | **GET** /phonenumber/ | Query for phone numbers in our inventory.
*PhonenumberApi* | [**phonenumber_num_post**](docs/PhonenumberApi.md#phonenumber_num_post) | **POST** /phonenumber/{num}/ | Buy number from inventory
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /webhook/ | Create webhooks to receive Message
*WebhookApi* | [**delete_webhook_by_id**](docs/WebhookApi.md#delete_webhook_by_id) | **DELETE** /webhook/{uid}/ | Delete a webhook by ID
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /webhook/ | Get a list of your webhooks
*WebhookApi* | [**get_webhook_by_id**](docs/WebhookApi.md#get_webhook_by_id) | **GET** /webhook/{uid}/ | Get a webhook by ID
*WebhookApi* | [**patch_webhook**](docs/WebhookApi.md#patch_webhook) | **PATCH** /webhook/{uid}/ | Edit a webhook


## Documentation For Models

 - [CreateAccount](docs/CreateAccount.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [Message](docs/Message.md)
 - [MessageQueued](docs/MessageQueued.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [MetaResponse](docs/MetaResponse.md)
 - [NumberWebhook](docs/NumberWebhook.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberRate](docs/PhoneNumberRate.md)
 - [PhoneNumberService](docs/PhoneNumberService.md)
 - [Webhook](docs/Webhook.md)
 - [ArrayMetaResponse](docs/ArrayMetaResponse.md)
 - [CreatedMetaResponse](docs/CreatedMetaResponse.md)
 - [EditableAccount](docs/EditableAccount.md)
 - [Number](docs/Number.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [Account](docs/Account.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

apiteam@mgageindia.com

