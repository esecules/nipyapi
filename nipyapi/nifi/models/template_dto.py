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


class TemplateDTO(object):
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
        'uri': 'str',
        'id': 'str',
        'group_id': 'str',
        'name': 'str',
        'description': 'str',
        'timestamp': 'str',
        'encoding_version': 'str',
        'snippet': 'FlowSnippetDTO'
    }

    attribute_map = {
        'uri': 'uri',
        'id': 'id',
        'group_id': 'groupId',
        'name': 'name',
        'description': 'description',
        'timestamp': 'timestamp',
        'encoding_version': 'encodingVersion',
        'snippet': 'snippet'
    }

    def __init__(self, uri=None, id=None, group_id=None, name=None, description=None, timestamp=None, encoding_version=None, snippet=None):
        """
        TemplateDTO - a model defined in Swagger
        """

        self._uri = None
        self._id = None
        self._group_id = None
        self._name = None
        self._description = None
        self._timestamp = None
        self._encoding_version = None
        self._snippet = None

        if uri is not None:
          self.uri = uri
        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if timestamp is not None:
          self.timestamp = timestamp
        if encoding_version is not None:
          self.encoding_version = encoding_version
        if snippet is not None:
          self.snippet = snippet

    @property
    def uri(self):
        """
        Gets the uri of this TemplateDTO.
        The URI for the template.

        :return: The uri of this TemplateDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TemplateDTO.
        The URI for the template.

        :param uri: The uri of this TemplateDTO.
        :type: str
        """

        self._uri = uri

    @property
    def id(self):
        """
        Gets the id of this TemplateDTO.
        The id of the template.

        :return: The id of this TemplateDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemplateDTO.
        The id of the template.

        :param id: The id of this TemplateDTO.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this TemplateDTO.
        The id of the Process Group that the template belongs to.

        :return: The group_id of this TemplateDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this TemplateDTO.
        The id of the Process Group that the template belongs to.

        :param group_id: The group_id of this TemplateDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this TemplateDTO.
        The name of the template.

        :return: The name of this TemplateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TemplateDTO.
        The name of the template.

        :param name: The name of this TemplateDTO.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TemplateDTO.
        The description of the template.

        :return: The description of this TemplateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TemplateDTO.
        The description of the template.

        :param description: The description of this TemplateDTO.
        :type: str
        """

        self._description = description

    @property
    def timestamp(self):
        """
        Gets the timestamp of this TemplateDTO.
        The timestamp when this template was created.

        :return: The timestamp of this TemplateDTO.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this TemplateDTO.
        The timestamp when this template was created.

        :param timestamp: The timestamp of this TemplateDTO.
        :type: str
        """

        self._timestamp = timestamp

    @property
    def encoding_version(self):
        """
        Gets the encoding_version of this TemplateDTO.
        The encoding version of this template.

        :return: The encoding_version of this TemplateDTO.
        :rtype: str
        """
        return self._encoding_version

    @encoding_version.setter
    def encoding_version(self, encoding_version):
        """
        Sets the encoding_version of this TemplateDTO.
        The encoding version of this template.

        :param encoding_version: The encoding_version of this TemplateDTO.
        :type: str
        """

        self._encoding_version = encoding_version

    @property
    def snippet(self):
        """
        Gets the snippet of this TemplateDTO.
        The contents of the template.

        :return: The snippet of this TemplateDTO.
        :rtype: FlowSnippetDTO
        """
        return self._snippet

    @snippet.setter
    def snippet(self, snippet):
        """
        Sets the snippet of this TemplateDTO.
        The contents of the template.

        :param snippet: The snippet of this TemplateDTO.
        :type: FlowSnippetDTO
        """

        self._snippet = snippet

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
        if not isinstance(other, TemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
