# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""This module contains a client that is responsible for providing x509 certificates that will eventually establish
 the authenticity of devices to Device Provisioning Service.
"""


class X509SecurityClient(object):
    """
    An X509 Security Client. This uses the certificate and key provided to authenticate a device
    with an Azure DPS instance.X509 Authentication is only supported for device identities
    connecting directly to an Azure DPS.
    """

    def __init__(self, provisioning_host, registration_id, id_scope, x509):
        """
        Initialize the X509 Certificate security client.
        :param provisioning_host: Host running the Device Provisioning Service. Can be found in the Azure portal in the
        Overview tab as the string Global device endpoint
        :param registration_id: The registration ID is used to uniquely identify a device in the Device Provisioning Service.
        The registration ID is alphanumeric, lowercase string and may contain hyphens.
        :param id_scope: The ID scope is used to uniquely identify the specific provisioning service the device will
        register through. The ID scope is assigned to a Device Provisioning Service when it is created by the user and
        is generated by the service and is immutable, guaranteeing uniqueness.
        :param x509: The x509 certificate, To use the certificate the enrollment object needs to contain cert (either the root certificate or one of the intermediate CA certificates).
        If the cert comes from a CER file, it needs to be base64 encoded.
        """
        self._provisioning_host = provisioning_host
        self._registration_id = registration_id
        self._id_scope = id_scope
        self._x509 = x509

    @property
    def provisioning_host(self):
        """
        :return: The registration ID is used to uniquely identify a device in the Device Provisioning Service.
        The registration ID is alphanumeric, lowercase string and may contain hyphens.
        """
        return self._provisioning_host

    @property
    def registration_id(self):
        """
        :return: The registration ID is used to uniquely identify a device in the Device Provisioning Service.
        The registration ID is alphanumeric, lowercase string and may contain hyphens.
        """
        return self._registration_id

    @property
    def id_scope(self):
        """
        :return: Host running the Device Provisioning Service.
        """
        return self._id_scope

    def get_x509_certificate(self):
        """
        :return: The x509 certificate, To use the certificate the enrollment object needs to contain
         cert (either the root certificate or one of the intermediate CA certificates).
        """
        return self._x509
