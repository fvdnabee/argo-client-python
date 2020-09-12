# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1SecretVolumeSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'default_mode': 'int',
        'items': 'list[V1KeyToPath]',
        'optional': 'bool',
        'secret_name': 'str'
    }

    attribute_map = {
        'default_mode': 'defaultMode',
        'items': 'items',
        'optional': 'optional',
        'secret_name': 'secretName'
    }

    def __init__(self, default_mode=None, items=None, optional=None, secret_name=None, local_vars_configuration=None):  # noqa: E501
        """V1SecretVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_mode = None
        self._items = None
        self._optional = None
        self._secret_name = None
        self.discriminator = None

        if default_mode is not None:
            self.default_mode = default_mode
        if items is not None:
            self.items = items
        if optional is not None:
            self.optional = optional
        if secret_name is not None:
            self.secret_name = secret_name

    @property
    def default_mode(self):
        """Gets the default_mode of this V1SecretVolumeSource.  # noqa: E501

        Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :return: The default_mode of this V1SecretVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """Sets the default_mode of this V1SecretVolumeSource.

        Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :param default_mode: The default_mode of this V1SecretVolumeSource.  # noqa: E501
        :type: int
        """

        self._default_mode = default_mode

    @property
    def items(self):
        """Gets the items of this V1SecretVolumeSource.  # noqa: E501

        If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.  # noqa: E501

        :return: The items of this V1SecretVolumeSource.  # noqa: E501
        :rtype: list[V1KeyToPath]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this V1SecretVolumeSource.

        If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.  # noqa: E501

        :param items: The items of this V1SecretVolumeSource.  # noqa: E501
        :type: list[V1KeyToPath]
        """

        self._items = items

    @property
    def optional(self):
        """Gets the optional of this V1SecretVolumeSource.  # noqa: E501

        Specify whether the Secret or its keys must be defined  # noqa: E501

        :return: The optional of this V1SecretVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this V1SecretVolumeSource.

        Specify whether the Secret or its keys must be defined  # noqa: E501

        :param optional: The optional of this V1SecretVolumeSource.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    @property
    def secret_name(self):
        """Gets the secret_name of this V1SecretVolumeSource.  # noqa: E501

        Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret  # noqa: E501

        :return: The secret_name of this V1SecretVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this V1SecretVolumeSource.

        Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret  # noqa: E501

        :param secret_name: The secret_name of this V1SecretVolumeSource.  # noqa: E501
        :type: str
        """

        self._secret_name = secret_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SecretVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SecretVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
