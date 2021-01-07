# coding: utf-8

"""
    Adobe Target Delivery API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Application(object):
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
        'id': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, version=None):  # noqa: E501
        """Application - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        Application ID. If not specified - all activities with any applicationId will be evaluated. If specified - only activities with the matching applicationId will be evaluated.   # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        Application ID. If not specified - all activities with any applicationId will be evaluated. If specified - only activities with the matching applicationId will be evaluated.   # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 250:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `250`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501

        Application name. If not specified - all activities with any applicationName will be evaluated. If specified - only activities with specified applicationName will be evaluated.   # noqa: E501

        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        Application name. If not specified - all activities with any applicationName will be evaluated. If specified - only activities with specified applicationName will be evaluated.   # noqa: E501

        :param name: The name of this Application.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this Application.  # noqa: E501

        Application version If not specified - all activities with any applicationVersion will not be evaluated. If specified - only activities with specific applicationVersion will be evaluated.   # noqa: E501

        :return: The version of this Application.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Application.

        Application version If not specified - all activities with any applicationVersion will not be evaluated. If specified - only activities with specific applicationVersion will be evaluated.   # noqa: E501

        :param version: The version of this Application.  # noqa: E501
        :type: str
        """
        if version is not None and len(version) > 128:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `128`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other