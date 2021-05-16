# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, IO, List, Optional, TYPE_CHECKING, Union

from azure.core.pipeline.transport._base import _format_url_section
from azure.purview.catalog.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_SERIALIZER = Serializer()


def build_query_request(
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Gets data using search.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :keyword json: An object specifying the search criteria.
    :paramtype json: Any
    :keyword content: An object specifying the search criteria.
    :paramtype content: Any
    :return: Returns an :class:`~azure.purview.catalog.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.catalog.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # JSON input template you can fill out and use as your `json` input.
            json = {
                "facets": [
                    {
                        "count": "int (optional)",
                        "facet": "str (optional)",
                        "sort": "object (optional)"
                    }
                ],
                "filter": "object (optional)",
                "keywords": "str (optional)",
                "limit": "int (optional)",
                "offset": "int (optional)",
                "taxonomySetting": {
                    "assetTypes": [
                        "str (optional)"
                    ],
                    "facet": {
                        "count": "int (optional)",
                        "facet": "str (optional)",
                        "sort": "object (optional)"
                    }
                }
            }


            # response body for status code(s): 200
            response_body == {
                "@search.count": "int (optional)",
                "@search.facets": {
                    "assetType": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "classification": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "classificationCategory": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "contactId": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "fileExtension": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "label": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ],
                    "term": [
                        {
                            "count": "int (optional)",
                            "value": "str (optional)"
                        }
                    ]
                },
                "value": [
                    {
                        "@search.highlights": {
                            "description": [
                                "str (optional)"
                            ],
                            "entityType": [
                                "str (optional)"
                            ],
                            "id": [
                                "str (optional)"
                            ],
                            "name": [
                                "str (optional)"
                            ],
                            "qualifiedName": [
                                "str (optional)"
                            ]
                        },
                        "@search.score": "float (optional)",
                        "@search.text": "str (optional)",
                        "assetType": [
                            "str (optional)"
                        ],
                        "classification": [
                            "str (optional)"
                        ],
                        "contact": [
                            {
                                "contactType": "str (optional)",
                                "id": "str (optional)",
                                "info": "str (optional)"
                            }
                        ],
                        "description": "str (optional)",
                        "entityType": "str (optional)",
                        "id": "str (optional)",
                        "label": [
                            "str (optional)"
                        ],
                        "name": "str (optional)",
                        "owner": "str (optional)",
                        "qualifiedName": "str (optional)",
                        "term": [
                            {
                                "glossaryName": "str (optional)",
                                "guid": "str (optional)",
                                "name": "str (optional)"
                            }
                        ]
                    }
                ]
            }

    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-05-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/search/query')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_suggest_request(
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Get search suggestions by query criteria.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :keyword json: An object specifying the suggest criteria.
    :paramtype json: Any
    :keyword content: An object specifying the suggest criteria.
    :paramtype content: Any
    :return: Returns an :class:`~azure.purview.catalog.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.catalog.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # JSON input template you can fill out and use as your `json` input.
            json = {
                "filter": "object (optional)",
                "keywords": "str (optional)",
                "limit": "int (optional)"
            }


            # response body for status code(s): 200
            response_body == {
                "value": [
                    {
                        "@search.score": "float (optional)",
                        "@search.text": "str (optional)",
                        "assetType": [
                            "str (optional)"
                        ],
                        "classification": [
                            "str (optional)"
                        ],
                        "contact": [
                            {
                                "contactType": "str (optional)",
                                "id": "str (optional)",
                                "info": "str (optional)"
                            }
                        ],
                        "description": "str (optional)",
                        "entityType": "str (optional)",
                        "id": "str (optional)",
                        "label": [
                            "str (optional)"
                        ],
                        "name": "str (optional)",
                        "owner": "str (optional)",
                        "qualifiedName": "str (optional)",
                        "term": [
                            {
                                "glossaryName": "str (optional)",
                                "guid": "str (optional)",
                                "name": "str (optional)"
                            }
                        ]
                    }
                ]
            }

    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-05-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/search/suggest')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_auto_complete_request(
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Get auto complete options.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :keyword json: An object specifying the autocomplete criteria.
    :paramtype json: Any
    :keyword content: An object specifying the autocomplete criteria.
    :paramtype content: Any
    :return: Returns an :class:`~azure.purview.catalog.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.catalog.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # JSON input template you can fill out and use as your `json` input.
            json = {
                "filter": "object (optional)",
                "keywords": "str (optional)",
                "limit": "int (optional)"
            }


            # response body for status code(s): 200
            response_body == {
                "value": [
                    {
                        "queryPlusText": "str (optional)",
                        "text": "str (optional)"
                    }
                ]
            }

    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-05-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/search/autocomplete')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

