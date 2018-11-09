# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.8.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RegistryDTO(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'uri': 'uri'
    }

    def __init__(self, id=None, name=None, description=None, uri=None):
        """
        RegistryDTO - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._uri = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if uri is not None:
          self.uri = uri

    @property
    def id(self):
        """
        Gets the id of this RegistryDTO.
        The registry identifier

        :return: The id of this RegistryDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RegistryDTO.
        The registry identifier

        :param id: The id of this RegistryDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RegistryDTO.
        The registry name

        :return: The name of this RegistryDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RegistryDTO.
        The registry name

        :param name: The name of this RegistryDTO.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RegistryDTO.
        The registry description

        :return: The description of this RegistryDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RegistryDTO.
        The registry description

        :param description: The description of this RegistryDTO.
        :type: str
        """

        self._description = description

    @property
    def uri(self):
        """
        Gets the uri of this RegistryDTO.
        The registry URI

        :return: The uri of this RegistryDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this RegistryDTO.
        The registry URI

        :param uri: The uri of this RegistryDTO.
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, RegistryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
