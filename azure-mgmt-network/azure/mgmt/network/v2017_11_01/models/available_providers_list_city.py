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


class AvailableProvidersListCity(Model):
    """City or town details.

    :param city_name: The city or town name.
    :type city_name: str
    :param providers: A list of Internet service providers.
    :type providers: list[str]
    """

    _attribute_map = {
        'city_name': {'key': 'cityName', 'type': 'str'},
        'providers': {'key': 'providers', 'type': '[str]'},
    }

    def __init__(self, city_name=None, providers=None):
        self.city_name = city_name
        self.providers = providers