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


class Screen(object):
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
        'width': 'float',
        'height': 'float',
        'color_depth': 'float',
        'pixel_ratio': 'float',
        'orientation': 'ScreenOrientationType'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height',
        'color_depth': 'colorDepth',
        'pixel_ratio': 'pixelRatio',
        'orientation': 'orientation'
    }

    def __init__(self, width=None, height=None, color_depth=None, pixel_ratio=None, orientation=None):  # noqa: E501
        """Screen - a model defined in OpenAPI"""  # noqa: E501

        self._width = None
        self._height = None
        self._color_depth = None
        self._pixel_ratio = None
        self._orientation = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if color_depth is not None:
            self.color_depth = color_depth
        if pixel_ratio is not None:
            self.pixel_ratio = pixel_ratio
        if orientation is not None:
            self.orientation = orientation

    @property
    def width(self):
        """Gets the width of this Screen.  # noqa: E501

        width  # noqa: E501

        :return: The width of this Screen.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Screen.

        width  # noqa: E501

        :param width: The width of this Screen.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Screen.  # noqa: E501

        height  # noqa: E501

        :return: The height of this Screen.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Screen.

        height  # noqa: E501

        :param height: The height of this Screen.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def color_depth(self):
        """Gets the color_depth of this Screen.  # noqa: E501

        color depth  # noqa: E501

        :return: The color_depth of this Screen.  # noqa: E501
        :rtype: float
        """
        return self._color_depth

    @color_depth.setter
    def color_depth(self, color_depth):
        """Sets the color_depth of this Screen.

        color depth  # noqa: E501

        :param color_depth: The color_depth of this Screen.  # noqa: E501
        :type: float
        """

        self._color_depth = color_depth

    @property
    def pixel_ratio(self):
        """Gets the pixel_ratio of this Screen.  # noqa: E501

        Optional, Used for device detection using the device atlas  # noqa: E501

        :return: The pixel_ratio of this Screen.  # noqa: E501
        :rtype: float
        """
        return self._pixel_ratio

    @pixel_ratio.setter
    def pixel_ratio(self, pixel_ratio):
        """Sets the pixel_ratio of this Screen.

        Optional, Used for device detection using the device atlas  # noqa: E501

        :param pixel_ratio: The pixel_ratio of this Screen.  # noqa: E501
        :type: float
        """

        self._pixel_ratio = pixel_ratio

    @property
    def orientation(self):
        """Gets the orientation of this Screen.  # noqa: E501


        :return: The orientation of this Screen.  # noqa: E501
        :rtype: ScreenOrientationType
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this Screen.


        :param orientation: The orientation of this Screen.  # noqa: E501
        :type: ScreenOrientationType
        """

        self._orientation = orientation

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
        if not isinstance(other, Screen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
