# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TransparentDataEncryptionsOperations:
    """TransparentDataEncryptionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.sql.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        transparent_data_encryption_name: Union[str, "_models.TransparentDataEncryptionName"],
        parameters: "_models.TransparentDataEncryption",
        **kwargs
    ) -> "_models.TransparentDataEncryption":
        """Creates or updates a database's transparent data encryption configuration.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param database_name: The name of the database for which setting the transparent data
         encryption applies.
        :type database_name: str
        :param transparent_data_encryption_name: The name of the transparent data encryption
         configuration.
        :type transparent_data_encryption_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :param parameters: The required parameters for creating or updating transparent data
         encryption.
        :type parameters: ~azure.mgmt.sql.models.TransparentDataEncryption
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TransparentDataEncryption, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.TransparentDataEncryption
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TransparentDataEncryption"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2014-04-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serverName': self._serialize.url("server_name", server_name, 'str'),
            'databaseName': self._serialize.url("database_name", database_name, 'str'),
            'transparentDataEncryptionName': self._serialize.url("transparent_data_encryption_name", transparent_data_encryption_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'TransparentDataEncryption')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TransparentDataEncryption', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TransparentDataEncryption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        transparent_data_encryption_name: Union[str, "_models.TransparentDataEncryptionName"],
        **kwargs
    ) -> "_models.TransparentDataEncryption":
        """Gets a database's transparent data encryption configuration.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param database_name: The name of the database for which the transparent data encryption
         applies.
        :type database_name: str
        :param transparent_data_encryption_name: The name of the transparent data encryption
         configuration.
        :type transparent_data_encryption_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TransparentDataEncryption, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.TransparentDataEncryption
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TransparentDataEncryption"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2014-04-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serverName': self._serialize.url("server_name", server_name, 'str'),
            'databaseName': self._serialize.url("database_name", database_name, 'str'),
            'transparentDataEncryptionName': self._serialize.url("transparent_data_encryption_name", transparent_data_encryption_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TransparentDataEncryption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName}'}  # type: ignore
