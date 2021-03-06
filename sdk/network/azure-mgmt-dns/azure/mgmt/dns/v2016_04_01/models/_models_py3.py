# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

import msrest.serialization

from ._dns_management_client_enums import *


class AaaaRecord(msrest.serialization.Model):
    """An AAAA record.

    :param ipv6_address: The IPv6 address of this AAAA record.
    :type ipv6_address: str
    """

    _attribute_map = {
        'ipv6_address': {'key': 'ipv6Address', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ipv6_address: Optional[str] = None,
        **kwargs
    ):
        super(AaaaRecord, self).__init__(**kwargs)
        self.ipv6_address = ipv6_address


class ARecord(msrest.serialization.Model):
    """An A record.

    :param ipv4_address: The IPv4 address of this A record.
    :type ipv4_address: str
    """

    _attribute_map = {
        'ipv4_address': {'key': 'ipv4Address', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ipv4_address: Optional[str] = None,
        **kwargs
    ):
        super(ARecord, self).__init__(**kwargs)
        self.ipv4_address = ipv4_address


class CloudErrorBody(msrest.serialization.Model):
    """An error response from the service.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable for display in a user
     interface.
    :type message: str
    :param target: The target of the particular error. For example, the name of the property in
     error.
    :type target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.dns.v2016_04_01.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["CloudErrorBody"]] = None,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class CnameRecord(msrest.serialization.Model):
    """A CNAME record.

    :param cname: The canonical name for this CNAME record.
    :type cname: str
    """

    _attribute_map = {
        'cname': {'key': 'cname', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        cname: Optional[str] = None,
        **kwargs
    ):
        super(CnameRecord, self).__init__(**kwargs)
        self.cname = cname


class MxRecord(msrest.serialization.Model):
    """An MX record.

    :param preference: The preference value for this MX record.
    :type preference: int
    :param exchange: The domain name of the mail host for this MX record.
    :type exchange: str
    """

    _attribute_map = {
        'preference': {'key': 'preference', 'type': 'int'},
        'exchange': {'key': 'exchange', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        preference: Optional[int] = None,
        exchange: Optional[str] = None,
        **kwargs
    ):
        super(MxRecord, self).__init__(**kwargs)
        self.preference = preference
        self.exchange = exchange


class NsRecord(msrest.serialization.Model):
    """An NS record.

    :param nsdname: The name server name for this NS record.
    :type nsdname: str
    """

    _attribute_map = {
        'nsdname': {'key': 'nsdname', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        nsdname: Optional[str] = None,
        **kwargs
    ):
        super(NsRecord, self).__init__(**kwargs)
        self.nsdname = nsdname


class PtrRecord(msrest.serialization.Model):
    """A PTR record.

    :param ptrdname: The PTR target domain name for this PTR record.
    :type ptrdname: str
    """

    _attribute_map = {
        'ptrdname': {'key': 'ptrdname', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ptrdname: Optional[str] = None,
        **kwargs
    ):
        super(PtrRecord, self).__init__(**kwargs)
        self.ptrdname = ptrdname


class RecordSet(msrest.serialization.Model):
    """Describes a DNS record set (a collection of DNS records with the same name and type).

    Variables are only populated by the server, and will be ignored when sending a request.

    :param id: The ID of the record set.
    :type id: str
    :param name: The name of the record set.
    :type name: str
    :param type: The type of the record set.
    :type type: str
    :param etag: The etag of the record set.
    :type etag: str
    :param metadata: The metadata attached to the record set.
    :type metadata: dict[str, str]
    :param ttl: The TTL (time-to-live) of the records in the record set.
    :type ttl: long
    :ivar fqdn: Fully qualified domain name of the record set.
    :vartype fqdn: str
    :param a_records: The list of A records in the record set.
    :type a_records: list[~azure.mgmt.dns.v2016_04_01.models.ARecord]
    :param aaaa_records: The list of AAAA records in the record set.
    :type aaaa_records: list[~azure.mgmt.dns.v2016_04_01.models.AaaaRecord]
    :param mx_records: The list of MX records in the record set.
    :type mx_records: list[~azure.mgmt.dns.v2016_04_01.models.MxRecord]
    :param ns_records: The list of NS records in the record set.
    :type ns_records: list[~azure.mgmt.dns.v2016_04_01.models.NsRecord]
    :param ptr_records: The list of PTR records in the record set.
    :type ptr_records: list[~azure.mgmt.dns.v2016_04_01.models.PtrRecord]
    :param srv_records: The list of SRV records in the record set.
    :type srv_records: list[~azure.mgmt.dns.v2016_04_01.models.SrvRecord]
    :param txt_records: The list of TXT records in the record set.
    :type txt_records: list[~azure.mgmt.dns.v2016_04_01.models.TxtRecord]
    :param cname_record: The CNAME record in the  record set.
    :type cname_record: ~azure.mgmt.dns.v2016_04_01.models.CnameRecord
    :param soa_record: The SOA record in the record set.
    :type soa_record: ~azure.mgmt.dns.v2016_04_01.models.SoaRecord
    """

    _validation = {
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'ttl': {'key': 'properties.TTL', 'type': 'long'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'a_records': {'key': 'properties.ARecords', 'type': '[ARecord]'},
        'aaaa_records': {'key': 'properties.AAAARecords', 'type': '[AaaaRecord]'},
        'mx_records': {'key': 'properties.MXRecords', 'type': '[MxRecord]'},
        'ns_records': {'key': 'properties.NSRecords', 'type': '[NsRecord]'},
        'ptr_records': {'key': 'properties.PTRRecords', 'type': '[PtrRecord]'},
        'srv_records': {'key': 'properties.SRVRecords', 'type': '[SrvRecord]'},
        'txt_records': {'key': 'properties.TXTRecords', 'type': '[TxtRecord]'},
        'cname_record': {'key': 'properties.CNAMERecord', 'type': 'CnameRecord'},
        'soa_record': {'key': 'properties.SOARecord', 'type': 'SoaRecord'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        etag: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        ttl: Optional[int] = None,
        a_records: Optional[List["ARecord"]] = None,
        aaaa_records: Optional[List["AaaaRecord"]] = None,
        mx_records: Optional[List["MxRecord"]] = None,
        ns_records: Optional[List["NsRecord"]] = None,
        ptr_records: Optional[List["PtrRecord"]] = None,
        srv_records: Optional[List["SrvRecord"]] = None,
        txt_records: Optional[List["TxtRecord"]] = None,
        cname_record: Optional["CnameRecord"] = None,
        soa_record: Optional["SoaRecord"] = None,
        **kwargs
    ):
        super(RecordSet, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.etag = etag
        self.metadata = metadata
        self.ttl = ttl
        self.fqdn = None
        self.a_records = a_records
        self.aaaa_records = aaaa_records
        self.mx_records = mx_records
        self.ns_records = ns_records
        self.ptr_records = ptr_records
        self.srv_records = srv_records
        self.txt_records = txt_records
        self.cname_record = cname_record
        self.soa_record = soa_record


class RecordSetListResult(msrest.serialization.Model):
    """The response to a record set List operation.

    :param value: Information about the record sets in the response.
    :type value: list[~azure.mgmt.dns.v2016_04_01.models.RecordSet]
    :param next_link: The continuation token for the next page of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RecordSet]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["RecordSet"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(RecordSetListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class RecordSetUpdateParameters(msrest.serialization.Model):
    """Parameters supplied to update a record set.

    :param record_set: Specifies information about the record set being updated.
    :type record_set: ~azure.mgmt.dns.v2016_04_01.models.RecordSet
    """

    _attribute_map = {
        'record_set': {'key': 'RecordSet', 'type': 'RecordSet'},
    }

    def __init__(
        self,
        *,
        record_set: Optional["RecordSet"] = None,
        **kwargs
    ):
        super(RecordSetUpdateParameters, self).__init__(**kwargs)
        self.record_set = record_set


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class SoaRecord(msrest.serialization.Model):
    """An SOA record.

    :param host: The domain name of the authoritative name server for this SOA record.
    :type host: str
    :param email: The email contact for this SOA record.
    :type email: str
    :param serial_number: The serial number for this SOA record.
    :type serial_number: long
    :param refresh_time: The refresh value for this SOA record.
    :type refresh_time: long
    :param retry_time: The retry time for this SOA record.
    :type retry_time: long
    :param expire_time: The expire time for this SOA record.
    :type expire_time: long
    :param minimum_ttl: The minimum value for this SOA record. By convention this is used to
     determine the negative caching duration.
    :type minimum_ttl: long
    """

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'serial_number': {'key': 'serialNumber', 'type': 'long'},
        'refresh_time': {'key': 'refreshTime', 'type': 'long'},
        'retry_time': {'key': 'retryTime', 'type': 'long'},
        'expire_time': {'key': 'expireTime', 'type': 'long'},
        'minimum_ttl': {'key': 'minimumTTL', 'type': 'long'},
    }

    def __init__(
        self,
        *,
        host: Optional[str] = None,
        email: Optional[str] = None,
        serial_number: Optional[int] = None,
        refresh_time: Optional[int] = None,
        retry_time: Optional[int] = None,
        expire_time: Optional[int] = None,
        minimum_ttl: Optional[int] = None,
        **kwargs
    ):
        super(SoaRecord, self).__init__(**kwargs)
        self.host = host
        self.email = email
        self.serial_number = serial_number
        self.refresh_time = refresh_time
        self.retry_time = retry_time
        self.expire_time = expire_time
        self.minimum_ttl = minimum_ttl


class SrvRecord(msrest.serialization.Model):
    """An SRV record.

    :param priority: The priority value for this SRV record.
    :type priority: int
    :param weight: The weight value for this SRV record.
    :type weight: int
    :param port: The port value for this SRV record.
    :type port: int
    :param target: The target domain name for this SRV record.
    :type target: str
    """

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'weight': {'key': 'weight', 'type': 'int'},
        'port': {'key': 'port', 'type': 'int'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        priority: Optional[int] = None,
        weight: Optional[int] = None,
        port: Optional[int] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(SrvRecord, self).__init__(**kwargs)
        self.priority = priority
        self.weight = weight
        self.port = port
        self.target = target


class SubResource(msrest.serialization.Model):
    """SubResource.

    :param id: Resource Id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(SubResource, self).__init__(**kwargs)
        self.id = id


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class TxtRecord(msrest.serialization.Model):
    """A TXT record.

    :param value: The text value of this TXT record.
    :type value: list[str]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List[str]] = None,
        **kwargs
    ):
        super(TxtRecord, self).__init__(**kwargs)
        self.value = value


class Zone(TrackedResource):
    """Describes a DNS zone.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param etag: The etag of the zone.
    :type etag: str
    :param max_number_of_record_sets: The maximum number of record sets that can be created in this
     DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
    :type max_number_of_record_sets: long
    :ivar max_number_of_records_per_record_set: The maximum number of records per record set that
     can be created in this DNS zone.  This is a read-only property and any attempt to set this
     value will be ignored.
    :vartype max_number_of_records_per_record_set: long
    :param number_of_record_sets: The current number of record sets in this DNS zone.  This is a
     read-only property and any attempt to set this value will be ignored.
    :type number_of_record_sets: long
    :ivar name_servers: The name servers for this DNS zone. This is a read-only property and any
     attempt to set this value will be ignored.
    :vartype name_servers: list[str]
    :param zone_type: The type of this DNS zone (Public or Private). Possible values include:
     "Public", "Private". Default value: "Public".
    :type zone_type: str or ~azure.mgmt.dns.v2016_04_01.models.ZoneType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'max_number_of_records_per_record_set': {'readonly': True},
        'name_servers': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'max_number_of_record_sets': {'key': 'properties.maxNumberOfRecordSets', 'type': 'long'},
        'max_number_of_records_per_record_set': {'key': 'properties.maxNumberOfRecordsPerRecordSet', 'type': 'long'},
        'number_of_record_sets': {'key': 'properties.numberOfRecordSets', 'type': 'long'},
        'name_servers': {'key': 'properties.nameServers', 'type': '[str]'},
        'zone_type': {'key': 'properties.zoneType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        etag: Optional[str] = None,
        max_number_of_record_sets: Optional[int] = None,
        number_of_record_sets: Optional[int] = None,
        zone_type: Optional[Union[str, "ZoneType"]] = "Public",
        **kwargs
    ):
        super(Zone, self).__init__(tags=tags, location=location, **kwargs)
        self.etag = etag
        self.max_number_of_record_sets = max_number_of_record_sets
        self.max_number_of_records_per_record_set = None
        self.number_of_record_sets = number_of_record_sets
        self.name_servers = None
        self.zone_type = zone_type


class ZoneDeleteResult(msrest.serialization.Model):
    """The response to a Zone Delete operation.

    :param azure_async_operation: Users can perform a Get on Azure-AsyncOperation to get the status
     of their delete Zone operations.
    :type azure_async_operation: str
    :param status:  Possible values include: "InProgress", "Succeeded", "Failed".
    :type status: str or ~azure.mgmt.dns.v2016_04_01.models.OperationStatus
    :param status_code:  Possible values include: "Continue", "SwitchingProtocols", "OK",
     "Created", "Accepted", "NonAuthoritativeInformation", "NoContent", "ResetContent",
     "PartialContent", "MultipleChoices", "Ambiguous", "MovedPermanently", "Moved", "Found",
     "Redirect", "SeeOther", "RedirectMethod", "NotModified", "UseProxy", "Unused",
     "TemporaryRedirect", "RedirectKeepVerb", "BadRequest", "Unauthorized", "PaymentRequired",
     "Forbidden", "NotFound", "MethodNotAllowed", "NotAcceptable", "ProxyAuthenticationRequired",
     "RequestTimeout", "Conflict", "Gone", "LengthRequired", "PreconditionFailed",
     "RequestEntityTooLarge", "RequestUriTooLong", "UnsupportedMediaType",
     "RequestedRangeNotSatisfiable", "ExpectationFailed", "UpgradeRequired", "InternalServerError",
     "NotImplemented", "BadGateway", "ServiceUnavailable", "GatewayTimeout",
     "HttpVersionNotSupported".
    :type status_code: str or ~azure.mgmt.dns.v2016_04_01.models.HttpStatusCode
    :param request_id:
    :type request_id: str
    """

    _attribute_map = {
        'azure_async_operation': {'key': 'azureAsyncOperation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'request_id': {'key': 'requestId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        azure_async_operation: Optional[str] = None,
        status: Optional[Union[str, "OperationStatus"]] = None,
        status_code: Optional[Union[str, "HttpStatusCode"]] = None,
        request_id: Optional[str] = None,
        **kwargs
    ):
        super(ZoneDeleteResult, self).__init__(**kwargs)
        self.azure_async_operation = azure_async_operation
        self.status = status
        self.status_code = status_code
        self.request_id = request_id


class ZoneListResult(msrest.serialization.Model):
    """The response to a Zone List or ListAll operation.

    :param value: Information about the DNS zones.
    :type value: list[~azure.mgmt.dns.v2016_04_01.models.Zone]
    :param next_link: The continuation token for the next page of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Zone]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Zone"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ZoneListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
