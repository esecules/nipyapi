# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.7.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NodeEventDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'timestamp': 'str',
        'category': 'str',
        'message': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'category': 'category',
        'message': 'message'
    }

    def __init__(self, timestamp=None, category=None, message=None):
        """
        NodeEventDTO - a model defined in Swagger
        """

        self._timestamp = None
        self._category = None
        self._message = None

        if timestamp is not None:
          self.timestamp = timestamp
        if category is not None:
          self.category = category
        if message is not None:
          self.message = message

    @property
    def timestamp(self):
        """
        Gets the timestamp of this NodeEventDTO.
        The timestamp of the node event.

        :return: The timestamp of this NodeEventDTO.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this NodeEventDTO.
        The timestamp of the node event.

        :param timestamp: The timestamp of this NodeEventDTO.
        :type: str
        """

        self._timestamp = timestamp

    @property
    def category(self):
        """
        Gets the category of this NodeEventDTO.
        The category of the node event.

        :return: The category of this NodeEventDTO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this NodeEventDTO.
        The category of the node event.

        :param category: The category of this NodeEventDTO.
        :type: str
        """

        self._category = category

    @property
    def message(self):
        """
        Gets the message of this NodeEventDTO.
        The message in the node event.

        :return: The message of this NodeEventDTO.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this NodeEventDTO.
        The message in the node event.

        :param message: The message of this NodeEventDTO.
        :type: str
        """

        self._message = message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NodeEventDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
