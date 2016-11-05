# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationGatewayBackendAddress(Model):
    """Backend address of an application gateway.

    :param fqdn: Fully qualified domain name (FQDN).
    :type fqdn: str
    :param ip_address: IP address
    :type ip_address: str
    """ 

    _attribute_map = {
        'fqdn': {'key': 'fqdn', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
    }

    def __init__(self, fqdn=None, ip_address=None):
        self.fqdn = fqdn
        self.ip_address = ip_address
